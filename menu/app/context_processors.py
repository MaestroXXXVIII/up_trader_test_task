def app_context(request):
    current_path_name = f'{request.scheme}://{request.get_host()}'
    return locals()