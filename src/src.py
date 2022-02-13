from activity.read_and_clean_data import *
from activity.make_viz import *
from activity.run_nlp import *
from utils.filter import *
from utils.utc_to_local import utc_to_local
from utils.math import analyze_time_series_data
from utils.get_nicknames import get_nicknames

# Read and clean data
data = read_data('/Users/danblevins/Desktop/message.json')
data['attachment'] = clean_and_update_attachments(data)
data['nickname'] = include_nickname_column(data)
data = filter_columns(data)

# Randomize names and rename columns
dictionary = randomize_names(data)
data["name"] = data["sender_id"].map(dictionary)
data = rename_columns(data)

# Clean columns more and filter by 2021
data['n_likes'] = clean_and_update_liked_by(data)
data['send_time'] = utc_to_local(data['send_time'])
data = filter_by_year(data, 2021)

# Transform name column and reset index
data['name_counts'] = data['name'].value_counts()
data['name_counts'] = data.groupby(['name']).transform('count')
data = filter_name_counts(data)
data = data.reset_index(drop=True)


# Descriptive NLP Analysis
# Avg Number of Likes per Message
names_group = data.groupby('name')
data_subset = names_group['n_likes'].mean()
data_subset = pd.DataFrame(data_subset)
data_subset.columns = ['avg_likes']
data_subset.reset_index(inplace=True)
data_subset = data_subset.sort_values(by=['avg_likes'], ascending=False)
bar_chart(data=data_subset, x_axis="name", y_axis="avg_likes", title="Most Popular (Avg Number of Likes per Message)", name="descr_nlp_fig1")

# Number of Messages Sent
data_subset = pd.DataFrame(data['name'].value_counts())
data_subset.reset_index(inplace=True)
data_subset.columns = ['name','msg_sent']
bar_chart(data=data_subset, x_axis="name", y_axis="msg_sent", title="Most Talkative (Number of Messages Sent)", name='descr_nlp_fig2')

# Avg Message Length
data['avg_message_len'] = data.message.str.split().str.len()
data_subset = data.groupby('name').avg_message_len.mean().sort_values(ascending=False).reset_index()
bar_chart(data=data_subset, x_axis="name", y_axis="avg_message_len", title="Most Verbose (Avg Message Length)", name='descr_nlp_fig3')

# Number of Times @ing Someone
ats = data[data.message.str.contains(" @")==True]
data_subset = ats.groupby("name").send_time.count().sort_values(ascending=False).reset_index()
data_subset.columns = ['name','ats']
bar_chart(data=data_subset, x_axis="name", y_axis="ats", title="Most Social (Number of Times @ing Someone)", name='descr_nlp_fig4')

# Number of Name Changes
nicknames_df = get_nicknames(data)
data_subset = nicknames_df.set_index("name").sort_values(by="length", ascending=False).reset_index()
data_subset.columns = ['name','name_changes']
bar_chart(data=data_subset, x_axis="name", y_axis="name_changes", title="Most Nicknames (Number of Name Changes)", name='descr_nlp_fig5')


# Time Series Analysis
time_series_complete = data.set_index('send_time')

# Avg Number of Likes by Month
time_series_subset = time_series_complete.resample('M').n_likes.mean()
data_subset = analyze_time_series_data(data=time_series_subset, column_name='avg_likes')
line_chart(data=data_subset, x_axis="month", y_axis="avg_likes", title="Avg Number of Likes by Month", name="time_series_fig1")

# Number of Messages by Month
time_series_subset = time_series_complete.resample('M').message.count()
data_subset = analyze_time_series_data(data=time_series_subset, column_name='n_likes')
line_chart(data=data_subset, x_axis="month", y_axis="n_likes", title="Number of Messages by Month", name="time_series_fig2")

# Textual NLP Analysis
text = data['message'].str.lower()
text = text.str.replace(r'\s*https?://\S+(\s+|$)', ' ').str.strip().replace('[^\w\s]','')
text = text.dropna().to_string(index=False).replace("\n", ' ').replace("\"", '').replace("\\n", ' ').replace("...", '')
text = remove_emoji(text)
# Tokenize and Lemmatize
text_tokenized_lemmatized = spacy_tokenizer_lemmatizer(text)
text_tokenized_lemmatized = [''.join(c for c in s if c not in punctuation) for s in text_tokenized_lemmatized]
text_tokenized_lemmatized = [s.strip() for s in text_tokenized_lemmatized]
text_tokenized_lemmatized = [s for s in text_tokenized_lemmatized if s]

result = find_ngram(text_tokenized_lemmatized)
ngram_bar_chart(data=result, x_axis="count", y_axis="word", title="Unigrams of Group", name='fig1')

result = find_ngram(text_tokenized_lemmatized, number_of_ngrams=2)
ngram_bar_chart(data=result, x_axis="count", y_axis="word", title="Bigrams of Group", name='fig2')

result = find_ngram(text_tokenized_lemmatized, number_of_ngrams=3)
ngram_bar_chart(data=result, x_axis="count", y_axis="word", title="Trigrams of Group", name='fig3')
