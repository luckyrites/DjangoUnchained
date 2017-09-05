from django.http import JsonResponse


class AjaxFormMixin(object):
	def form_invalid(self,form):
		response = super(AjaxFormMixin,self).form_invalid(form)
		if self.request.is_ajax():
			print(form.errors)
			return JsonResponse(form.errors,status=404)
		else:
			return response

	def form_valid(self,form):
		response = super(AjaxFormMixin,self).form_valid(form)
		if self.request.is_ajax():
			print(form.cleaned_data)
			data = {
				'message': "Submitted Successfully the form data"
			}
			return JsonResponse(data)
		else:
			return response
