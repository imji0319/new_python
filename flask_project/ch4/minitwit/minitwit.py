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



