from django.contrib import admin
# Register your models here.

from .models import Todo
from .models import About
from .models import Project
from .models import Post
from .models import Comment


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','description','completed')

class AboutAdmin(admin.ModelAdmin):
    list_display = ('name','story')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_title','project_description','project_start','project_end','project_author')

class PostAdmin(admin.ModelAdmin):
    list_display=('post_title','post_image','post_brief','post_content','post_publish_date','post_author','post_category')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_id','comment_author_id','comment_content','comment_email')



admin.site.register(Todo,TodoAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
