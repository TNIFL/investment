from flask import Blueprint, request, render_template, session, redirect, flash, url_for
from app.services.community_service import *

community = Blueprint('community', __name__)


@community.route('/community', methods=['GET','POST'])
def community_page():
    #TODO::구현해야 할 기능 / 게시글 CRUD, 댓글 CRUD, 글 좋아요, 글 조회수 표시
    user_id = session.get('id')
    posts = get_post_data_from_db()
    #TODO::ID 확인 부터 시작함. ID = None 이면 글 읽기만 가능함
    if request.method == 'GET':
        if user_id:
            print(user_id, 'session 정보를 가져오는데 성공')
        else:
            print(user_id, 'session 정보를 가져오는데 실패')
        return render_template('community/list.html', id=user_id, posts=posts)
    if request.method == 'POST':
        return render_template('community/list.html', id=user_id, posts=posts)


@community.route('/community/<int:post_id>', methods=['GET', 'POST'])
def post_detail(post_id):
    user_id = session.get('id')
    post = get_post_by_post_id(post_id)
    comments = get_comment_by_post_id(post_id)
    increment_click_count_result = increment_click_count(post_id)
    print(increment_click_count_result)
    print('현재 session id : ', user_id)
    print('가져온 댓글 : ', comments)

    if request.method == 'GET':
        return render_template('community/detail.html', post=post,
                                                        comments=comments,
                                                        id=user_id)
    if request.method == 'POST':
        insert_comment = request.form.get('write-comment')
        #insert_result = insert_comment_by_post_id(insert_comment, post_id, user_id)

        try:
            insert_result = insert_comment_by_post_id(post_id, user_id, insert_comment)
            if insert_result:
                flash('댓글이 등록되었습니다.')
            else:
                flash('댓글 등록에 실패했습니다.')

        except Exception as e:
            print('댓글 작성 중 오류 발생 : ', e)
            flash('서버 오류로 댓글 등록에 실패했습니다.')
        return redirect(url_for('community.post_detail', id=user_id,
                                                         post_id=post_id))





@community.route('/community/write', methods=['GET', 'POST'])
def post_write():
    user_id = session.get('id')

    if id == 'None':
        return redirect('/community', message='로그인 필요')

    if request.method == 'GET':
        return render_template('community/write.html', id=user_id)

    if request. method == 'POST':       #TODO::글 작성 후 연결되는 루트는 list가 아니라 detail(내가 쓴 글)로 가야함
        title = request.form.get('title')
        content = request.form.get('content')
        print('---------------community.route------------------')
        print('루트에서 인식되는 사용자 id : ', user_id)
        result = create_post(user_id, title, content)
        posts = get_post_data_from_db()         #post_id를 내가 쓴 글의 title을 참조해서 가져오기 -> db연결 --- get_post_id_by_post_title
        post_id_data = get_post_id_from_post_title(title)

        if post_id_data and 'id' in post_id_data:
            return redirect(url_for('community.post_detail', post_id=int(post_id_data['id'])))


        return redirect('/community')


@community.route('/community/mypage/<int:user_id>', methods=['GET', 'POST'])
def post_mypage(user_id):
    user_id = session.get('id')

    if not id:
        return redirect('/community', message='로그인 필요')
    return render_template('community/mypage', user_id=user_id)

@community.route('/community/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_page(post_id):
    #edit페이지로 넘어오기 전에도 애초에 내 게시글이 아니면 수정 못하게 되어있었음
    #그래도 혹시 모르니 post_id로 post_user_id를 조회 후 현재 session에 있는 id와 비교 -> 수정 y/n
    print('현재 이 post의 post_id 는 ', post_id, '입니다.')
    user_id = session.get('id')
    post = get_post_by_post_id(post_id)
    print(post_id, '로 불러온 post의 정보는 ', post, '입니다.')



    if request.method == 'GET':
        return render_template('community/edit.html', post=post,
                                                      user_id=user_id)

    if request.method == 'POST':
        updated_title = request.form.get('title-edit')
        updated_content = request.form.get('content-edit')

        result = update_post(post_id, updated_title, updated_content)

        if result:
            flash('게시글을 수정했습니다.')
            return redirect(url_for('community.post_detail', post_id=post_id))

        return render_template('community/edit.html', post=post,
                                                      user_id=user_id)



    return None