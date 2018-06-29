import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)
# print(response.status_code)
response_dict = response.json()
response_dicts = response_dict['items']
names, plot_dicts = [], []
for repos_dict in response_dicts:
    names.append(repos_dict['name'])

    plot_dict = {
        'value': repos_dict['stargazers_count'],  # 每个project的star数量
        'label': repos_dict['description'],  # 鼠标放在图上显示对应project的描述信息
        'xlink': repos_dict['html_url'],  # 在每个project加上对应的url链接,展示的时候点击即可打开相应链接
    }
    plot_dicts.append(plot_dict)
# print(plot_dicts)

"""定制图表样式"""
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('Python_repos_enhance.svg')



