from django.contrib import admin
from app01.models import Customer,Apps,DeviceAppUpdate
import requests


class CustomerAdmin(admin.ModelAdmin):
	list_display = ['name','updated']



class AppsAdmin(admin.ModelAdmin):
	list_display = ['displayName','packageName']


class DeviceAppUpdateAdmin(admin.ModelAdmin):
	list_display = ['UID','customer','app','isUpdated']

	# 定制Action行为具体方法
	def is_update(self, request, queryset):
		for update_obj in queryset:
			update_obj.isUpdated = True
			update_obj.save()
		# print(request.POST.getlist('_selected_action'))

	def not_update(self, request, queryset):
		for update_obj in queryset:
			update_obj.isUpdated = False
			update_obj.save()

	def save_model(self, request, obj, form, change):
		print('-'*100)
		print('save mode.......')
		print('path:  ',request.path)
		# print('form:  ',form)
		print('change:  ',change)
		print('method:  ',request.method)
		# print('obj:  ',obj)
		print('-'*100)
		"""
		Given a model instance save it to the database.
		"""
		obj.save()

	is_update.short_description = "标记为更新"
	not_update.short_description = "标记为不更新"
	actions = [is_update, not_update,]

	# Action选项都是在页面上方显示
	actions_on_top = True
	# Action选项都是在页面下方显示
	actions_on_bottom = False

	# 是否显示选择个数
	actions_selection_counter = True


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Apps,AppsAdmin)
admin.site.register(DeviceAppUpdate,DeviceAppUpdateAdmin)