from django.core.management.base import BaseCommand
from ...models import *
import datetime


class Command(BaseCommand):
    help = 'Fill database but likes quantity on each question equals 1 or 3'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int)

    def handle(self, *args, **options):
        start = datetime.datetime.now()
        ratio = options.get('ratio')
        num_users = ratio
        #  num_questions = ratio * 10
        #  num_answers = ratio * 100
        #  num_likes_dislikes = ratio * 200

        for i in range(1, (num_users + 1)):
            # fill user                                 ## USER filled
            user = User(
                username='username%i' % i,
                first_name='username%i' % i,
                email='username%i@mail.ru' % i,
                date_joined=datetime.datetime.now(),
                is_active=False,
            )
            user.set_password('password%i' % i)
            user.save()
            # fill like                                 ## LIKE filled
            like = Like(
                user_id=user.pk,
            )
            like.save()
            # fill profile                              ## PROFILE partially filled (rating)
            profile = Profile(
                avatar='web/main/static/img/default_avatar.svg',
                rating=0,
                user_fk_id=user.pk,
            )
            profile.save()
            # fill tags                                 ## TAG partially filled (.questions.add())
            tag = Tag(
                tag='tag%i' % i,
            )
            tag.save()
            # fill questions
            for j in range(1, 11):
                # fill question                             ## QUESTION filled
                question = Question(
                    title='title title title title title',
                    descr='title title title title title...'
                          ' title title title title title..'
                          'title title title title title...'
                          'title title title title title...'
                          'title title title title title',
                    author_fk_id=user.pk,
                    date=datetime.datetime.now(),
                )
                question.save()
                # fill tag                                  ## TAG filled
                tag.questions.add(question)
                tag.save()
                # fill q_like                               ## QUESTION_LIKE filled
                if i % 3 == 0:
                    for i in range(1, 4):
                        q_like = QuestionLike(
                            like=1,
                            question_id=question.pk,
                            q_like_id=like.pk,
                        )
                        q_like.save()
                else:
                    q_like = QuestionLike(
                        like=1,
                        question_id=question.pk,
                        q_like_id=like.pk,
                    )
                    q_like.save()
                # fill answer                               ## ANSWER filled
                if j % 10 == 0:
                    for k in range(1, 56):
                        if k == 25:
                            answer = Answer(
                                descr='title title title title title...'
                                      ' title title title title title..'
                                      'title title title title title...'
                                      'title title title title title...'
                                      'title title title title title',
                                correct=True,
                                author_fk_id=user.pk,
                                question_fk_id=question.pk,
                                date=datetime.datetime.now(),
                            )
                            answer.save()
                            a_like = AnswerLike(
                                like=1,
                                answer_id=answer.pk,
                                a_like_id=like.pk,
                            )
                            a_like.save()
                        else:
                            answer = Answer(
                                descr='title title title title title...'
                                      ' title title title title title..'
                                      'title title title title title...'
                                      'title title title title title...'
                                      'title title title title title',
                                correct=False,
                                author_fk_id=user.pk,
                                question_fk_id=question.pk,
                                date=datetime.datetime.now(),
                            )
                            answer.save()
                            a_like = AnswerLike(
                                like=1,
                                answer_id=answer.pk,
                                a_like_id=like.pk,
                            )
                            a_like.save()
                else:
                    for k in range(1, 6):
                        if k == 3:
                            answer = Answer(
                                descr='title title title title title...'
                                      ' title title title title title..'
                                      'title title title title title...'
                                      'title title title title title...'
                                      'title title title title title',
                                correct=True,
                                author_fk_id=user.pk,
                                question_fk_id=question.pk,
                                date=datetime.datetime.now(),
                            )
                            answer.save()
                            a_like = AnswerLike(
                                like=1,
                                answer_id=answer.pk,
                                a_like_id=like.pk,
                            )
                            a_like.save()
                        else:
                            answer = Answer(
                                descr='title title title title title...'
                                      ' title title title title title..'
                                      'title title title title title...'
                                      'title title title title title...'
                                      'title title title title title',
                                correct=False,
                                author_fk_id=user.pk,
                                question_fk_id=question.pk,
                                date=datetime.datetime.now(),
                            )
                            answer.save()
                            a_like = AnswerLike(
                                like=1,
                                answer_id=answer.pk,
                                a_like_id=like.pk,
                            )
                            a_like.save()

        stop = datetime.datetime.now()

        print("Script start : %s" % start)
        print("Script stop : %s" % stop)

