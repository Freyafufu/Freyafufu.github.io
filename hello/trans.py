from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/user')
# def get_user():
#     # 从 GET 请求的查询参数中获取名为 'name' 的值
#     name = request.args.get('name')
#     print(name)
#     if name == 'zxj':
#         return dict(name = 'zxj from GET',age = 20)
#     else:
#         return dict(name = 'bushi zxj from GET',age = 30)
    
# @app.route('/user',methods=['POST'])
# def post_user():
#     # 打印POST请求的原始数据
#     print(request.data)
#     # 将请求体中的数据解析为 JSON 格式
#     print(request.json)
#     name = request.json.get("name")
#     if name == 'zxj':
#         return dict(name = 'zxj from POST',age = 20)
#     else:
#         return dict(name = 'bushi zxj from POST',age = 30)

# @app.route('/user',methods = ['GET','POST'])
# def trans_user():
#     if request.method == 'GET':
#         name = request.args.get('name')
#         print(name)
#         if name == 'zxj':
#             return dict(name = 'zxj from GET',age = 20)
#         else:
#             return dict(name = 'bushi zxj from GET',age = 30)
#     elif request.method == 'POST':
#         print(request.data)
#         print(request.json)
#         name = request.json.get("name")
#         if name == 'zxj':
#             return dict(name = 'zxj from POST',age = 20)
#         else:
#             return dict(name = 'bushi zxj from POST',age = 30)

# 文件上传、表单提交
import os
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['POST'])
def upload():
    form_data = request.form  # 获取表单数据
    file_data = request.files  # 获取文件数据

    # 将表单数据和文件数据的名称存放到一个列表中
    data_list = []
    for key, value in form_data.items():
        data_list.append(f'{key}:{value}')
    for key, file in file_data.items():
        data_list.append(f'{key}:{file.filename}')

    # 读取文件中已有的内容
    existing_content = ''
    with open('static/uploads/data.txt', 'r') as file:
        existing_content = file.read()

    # 检查文件是否为空
    if existing_content:
        existing_content += '\n'

    # 将新内容和已有内容写入到一个 txt 文件中
    with open('static/uploads/data.txt', 'w') as file:
        file.write(existing_content + ' '.join(data_list))

    # 创建以id命名的文件夹
    id_folder = "id_"+form_data.get('id')
    folder_path = os.path.join('static/uploads/', id_folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 保存上传的图片文件到对应的文件夹中
    photo_file = request.files.get('photo')
    filename = secure_filename(photo_file.filename)
    photo_file.save(os.path.join(folder_path, filename))

    return 'Successfully!'


@app.route('/show')
def display():
    contents = []
    with open('static/uploads/data.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split()
            content = {
                'id': '',
                'name': '',
                'balance': '',
                'photo': ''
            }
            for item in data:
                key, value = item.split(':')
                if key == 'id':
                    content['id'] = value
                elif key == 'name':
                    content['name'] = value
                elif key == 'balance':
                    content['balance'] = value
                elif key == 'photo':
                    content['photo'] = value
            contents.append(content)

    return render_template('data.html', contents=contents)

if __name__ == '__main__':
    app.run(debug=True)
