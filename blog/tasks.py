from celery import shared_task
from random import choice
from django.utils import timezone
from celery.schedules import crontab
from blog.models import Comment, Post


@shared_task(name=' View all Comments and Auto Reply')
def reply_to_comments():
    comments = Comment.objects.all()
    for comment in comments:
        if comment.reply:
            continue
        replies = ["Thank you for your comment!", "We appreciate your feedback.", "Your comment has been noted."]
        reply = choice(replies)
        comment.reply = reply
        comment.save()


#
# @periodic_task(run_every=crontab(hour=0, minute=0))
# def run_reply_to_comments_task():
#    reply_to_comments.delay()