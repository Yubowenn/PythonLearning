from flask import Flask, abort, g

app = Flask(__name__)

@app.before_request
def authenticate():
    # 在进入所有视图之前，判断用户身份
    # g.user_id = 123 # 将用户信息存在g对象中
    g.user_id = None

# 强制登陆装饰器
def login_required(func):
    
    def wrapper(*args, **kwargs):
        # 判断用户是否登陆
        if g.user_id is None:
            abort(401)
        else:
            return func(*args, **kwargs)
    
    return wrapper

@app.route('/')
def index():
    return 'home page user_id={}'.format(g.user_id)

@app.route('/profile')
@login_required
def get_user_profile():
    return 'user profile page user_id={}'.format(g.user_id)

if __name__ == '__main__':
    app.run()