import os
from flask import Flask, render_template, flash, redirect
from flask import url_for, request, send_from_directory
import audit_helper

if os.getcwd() == '/home/lmn':
    os.chdir('/home/lmn/audit_helper')
app = Flask(__name__)
app.secret_key = 'lalalalololo'
app.config.from_pyfile('settings.py')
cs = audit_helper.cs


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    print(request.form)
    if request.form.get('type'):
        data = request.form.get('data')
        if not data:
            flash('没有输入搜索内容！')
        elif data in cs.course_names:
            return render_template('wait.html')
        else:
            return render_template('confirm.html', possibles=cs.search(data))


@app.route('/get_class')
def get_class():
    print(request.args.get('data'))
    data = request.args.get('data')
    if data not in cs.course_names:
        return render_template('wait.html')
    else:
        return render_template('show.html',
                               data=cs.get_data_by_course_name(data))


@app.route('/class_list')
def class_list():
    return render_template('class_list.html',
                           classes=cs.course_names)
