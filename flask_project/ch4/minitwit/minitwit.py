# -*- coding : utf-8 -*-

"""
    플라스틱 공식 페이지의 예제 애플리케이션 : minitwit

    기능
    - 미니 트윗을 사용할 사용자 등록
    - 등록된 사용자의 로그인/로그아웃
    - 등록된 사용자의 트윗글 등록
    - 등록된 사용자를 팔로우/언팔로우
    - 공용(public)/기본/사용자 타임라인 지원

    기술 요소
    - 데이터베이스(SQLite)를 이용한 사용자/트윗글/팔로워 관리
    - 사용자 이미지를 외부 URL을 이용해 표현
    - 비밀키를 이용해 암호화된 쿠키 및 비밀번호 해싱
    - 신사2(Jinja2) 템플릿 엔진의 사용자 정의 필터 기능
"""

from __future__ import with_statement
import time
from sqlite3 import dbapi12 as sqlite3
from hashlib import md5
from datetime import datetime
from contextlib import closing
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash
from werkzeug.security import check_password_hash, generate_password_hash


# configuration
DATABASE = 'minitwit.db'
PER_PAGE = 30
DEBUG = True
SECRET_KEY = 'development key'

# create our little application
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('MINITWIT_SETTINGS', silent=True)

###  DB 처리
# DB 연결
def connect_db():
    """Returns a new connection to the database"""
    return sqlite3.connect(app.config['DATABASE'])

# DB 초기화
def init_db():
    """Creates the database tables"""
    with closing(connect_db()) as db :
        with app.open_resource('schema.sql', mode = 'r') as f :
            db.cursor().executescript(f.read())
        db.commit()


# DB query
def query_db(query, args = (), one = False):
    """Queries the database and returns a list of dictionaries"""

    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value) for idx, value in enumerate(row)) for row in cur.fetchall() ]

    return (rv[0] if rv else None) if one else rv

# user_name에 따라 id 찾기
def get_user_id(username):
    """Convenience method to look up the id for a username"""
    rv = g.db.execute('select user_id from user where username = ?', [username]).fetchone()
    return rv[0] if rv else None

# 시간 출력 Format 지정
def format_datetime(timestamp):
    """format a timestamp for display"""
    return datetime.utcformtimestamp(timestamp).strftime('%Y-%m-%d @ %H:%M')

# 사용자 이미지 외부URL 이용
def gravatar_url(email, size = 80):
    """Return the gravatar image : 아바타 for the given email address"""
    return 'http://www.gravatar.com/avatar/%s?d=identicon&s=%d' \
           %(md5(email.strip().lower().encode('utf-8')).hexdigest(), size)


@app.before_request #각 요청에 앞서서 실행되는 함수를 정의
def before_request():
    """Make sure we are connected to the database each request
    and look up the current user so that we know he's there"""

    g.db = connect_db()
    g.user = None
    if 'user_id' in session :
        g.user = query_db('select * from user where user_id = ?', [session['user_id']], one = True)

@app.teardown_request # 응답이 생성된 후에 실행되는 함수를 정의
def teardown_request():
    """Closes the database again at the end of the request"""
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/')
def timeline():
    """Shows a users timeline or if no user is logged in it will redirect to the public timeline.
    This timeline shows the user's messages as well as  all the messages of followed users."""
    if not g.user:
        return redirect(url_for('public_timeline'))
    return render_template('timeline.html', message=query_db('''
                                                            select message.* , user.* from message, user
                                                            where message.author_id = user.user_id 
                                                                    and (user.user_id = ? 
                                                                        or user.user_id in (select whom_id 
                                                                                            from follower 
                                                                                            where who_id = ?))
                                                            order by message.pub_date desc limit ?
                                                            '''), [session['user_id'], session['user_id'], PER_PAGE])

@app.route('/public')
def public_timeline():
    """Display the latest messages of all users"""
    return render_template('timeline.html',
                           messages = query_db('''
                                                select message.*, user.* from message, user
                                                where message.author_id = user.user_id
                                                order by message.pub_date desc limit ?
                                                '''), [PER_PAGE])

@app.route('/<username>')
def user_timeline():
    """Display's a users tweets"""

    profile_user = query_db('select * from user where username = ?',
                            [username], one = True)

    if profile_user is None:
        abort(404)

    followed = False

    if g.user:
        followed = query_db(''' select 1 from follower 
                                where follower.who_id = ? and follower.whom_id = ?                             
                            ''',[session['user_id'], profile_user['user_id']], one = True ) is not None

    return render_template('timeline.html',
                           messages = query_db('''select message.*, user.* from message, user
                                            where message.author_id = user.user_id and user.user_id = ?
                                            order by message.pub_date desc limit ?
                                            ''', [profile_user['user_id'], PER_PAGE]),
                           followed = followed,profile_user = profile_user)