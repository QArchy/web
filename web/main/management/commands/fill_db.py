import random
from django.core.management.base import BaseCommand
from ...models import Question, Answer, Tag, Profile, MyUser
import datetime


class Command(BaseCommand):
    help = 'Fill database'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int)

    def handle(self, *args, **options):
        start = datetime.datetime.now()
        ratio = options.get('ratio')
        num_users = ratio
        num_questions = ratio * 10
        num_answers = ratio * 100
        num_tags = ratio
        num_likes_dislikes = ratio * 200

        for i in range(1, (num_users + 1)):
            # fill user
            user = MyUser(
                password='password%i' % i,
                username='username%i' % i,
                email='username%i@mail.ru' % i,
                date_joined=datetime.datetime.now(),
                is_active=False,
            )
            user.save()
            # fill profile
            profile = Profile(
                avatar='/home/artem/PycharmProjects/webHomework/web/main/static/img/default_avatar.svg',
                rating=0,
                user_fk_id=user.pk,
            )
            profile.save()
            # gen tags
            tag = Tag(
                tag='tag%i' % i,
            )
            tag.save()
            # fill questions
            for j in range(1, 11):
                _likes = random.randint(0, 200)
                _dislikes = 200 - _likes
                # adjust user rating
                profile.rating = profile.rating + _likes - _dislikes
                profile.save()
                #
                question = Question(
                    title='title title title title title',
                    descr='title title title title title...'
                          ' title title title title title..'
                          'title title title title title...'
                          'title title title title title...'
                          'title title title title title',
                    likes=_likes,
                    dislikes=_dislikes,
                    author_fk_id=user.pk,
                    date=datetime.datetime.now(),
                )
                question.save()
                tag.questions.add(question)

                if j % 10 == 0:
                    for k in range(1, 56):
                        # adjust user rating
                        profile.rating = profile.rating + _likes - _dislikes
                        profile.save()
                        #
                        if k == 25:
                            answer = Answer(
                                descr='title title title title title...'
                                      ' title title title title title..'
                                      'title title title title title...'
                                      'title title title title title...'
                                      'title title title title title',
                                likes=_likes,
                                dislikes=_dislikes,
                                correct=True,
                                author_fk_id=user.pk,
                                question_fk_id=question.pk,
                                date=datetime.datetime.now(),
                            )
                            answer.save()
                        else:
                            answer = Answer(
                                descr='title title title title title...'
                                      ' title title title title title..'
                                      'title title title title title...'
                                      'title title title title title...'
                                      'title title title title title',
                                likes=_likes,
                                dislikes=_dislikes,
                                correct=False,
                                author_fk_id=user.pk,
                                question_fk_id=question.pk,
                                date=datetime.datetime.now(),
                            )
                            answer.save()
                else:
                    for k in range(1, 6):
                        # adjust user rating
                        profile.rating = profile.rating + _likes - _dislikes
                        profile.save()
                        #
                        if k == 3:
                            answer = Answer(
                                descr='title title title title title...'
                                      ' title title title title title..'
                                      'title title title title title...'
                                      'title title title title title...'
                                      'title title title title title',
                                likes=_likes,
                                dislikes=_dislikes,
                                correct=True,
                                author_fk_id=user.pk,
                                question_fk_id=question.pk,
                                date=datetime.datetime.now(),
                            )
                            answer.save()
                        else:
                            answer = Answer(
                                descr='title title title title title...'
                                      ' title title title title title..'
                                      'title title title title title...'
                                      'title title title title title...'
                                      'title title title title title',
                                likes=_likes,
                                dislikes=_dislikes,
                                correct=False,
                                author_fk_id=user.pk,
                                question_fk_id=question.pk,
                                date=datetime.datetime.now(),
                            )
                            answer.save()

        stop = datetime.datetime.now()

        def print_info():
            print("Ratio : %s" % ratio)
            print("Users : %s" % num_users)
            print("Questions : %s" % num_questions)
            print("Answers : %s" % num_answers)
            print("Tags : %s" % num_tags)
            print("Likes and dislikes : %s" % num_likes_dislikes)
            print("Script start : %s" % start)
            print("Script stop : %s" % stop)

        print_info()
