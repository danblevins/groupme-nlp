from activity.read_and_clean_data import *
from activity.make_viz import *
from activity.run_nlp import *
from utils.filter import *
from utils.utc_to_local import utc_to_local
from utils.math import groupby_transform
from utils.get_nicknames import get_nicknames

# Read, clean, and filter data
data = read_data('data')
data['attachment'] = clean_and_update_attachments(data)
data['nickname'] = include_nickname_column(data)
data = filter_columns(data)

dictionary = randomize_names(data)
data["name"] = data["sender_id"].map(dictionary)

data = rename_columns(data)

data['n_likes'] = clean_and_update_liked_by(data)

data['send_time'] = utc_to_local(data['send_time'])
data = filter_by_year(data, 2021)

data['name_counts'] = groupby_transform(data, 'name', 'count')
data = filter_name_counts(data)
data = data.reset_index(drop=True)

# Descriptive NLP Analysis
names_group = data.groupby('name')
data_subset = names_group['n_likes'].mean()
data_subset = pd.DataFrame(data_subset)
data_subset.columns = ['avg_likes']
data_subset.reset_index(inplace=True)
data_subset = data_subset.sort_values(by=['avg_likes'], ascending=False)
bar_chart(data=data_subset, x_axis="name", y_axis="avg_likes", title="Most Popular (Avg Number of Likes per Message)", name="fig1")

data_subset = pd.DataFrame(data['name'].value_counts())
data_subset.reset_index(inplace=True)
data_subset.columns = ['name','msg_sent']
bar_chart(data=data_subset, x_axis="name", y_axis="msg_sent", title="Most Talkative (Number of Messages Sent)", name='fig2')

data['avg_message_len'] = data.message.str.split().str.len()
data_subset = data.groupby('name').avg_message_len.mean().sort_values(ascending=False).reset_index()
bar_chart(data=data_subset, x_axis="name", y_axis="avg_message_len", title="Most Verbose (Avg Message Length)", name='fig3')

ats = data[data.message.str.contains(" @")==True]
data_subset = ats.groupby("name").send_time.count().sort_values(ascending=False).reset_index()
data_subset.columns = ['name','ats']
bar_chart(data=data_subset, x_axis="name", y_axis="ats", title="Most Social (Number of Times @ing Someone)", name='fig4')

nicknames_df = get_nicknames(data)
data_subset = nicknames_df.set_index("name").sort_values(by="length", ascending=False).reset_index()
data_subset.columns = ['name','name_changes']
bar_chart(data=data_subset, x_axis="name", y_axis="name_changes", title="Most Nicknames (Number of Name Changes)", name='fig5')

# Time Series Analysis
time_series_complete = data.set_index('send_time')
data_subset = analyze_time_series_data(data, column_name)
