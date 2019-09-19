from django.shortcuts import render

# Create your views here.
def test(request):
    return   render(request,'index.html')
    

######
def get_app(request):
    app_list = []
    client = get_client_by_request(request)
    kwargs = {}
    resp  = client.cc.get_app_list(**kwargs)
    
    if resp.get('result'):
        data = resp.get('data',[])
        for _d in data:
            app_list.append({
                'name': _d.get('ApplicationName'),
                'id':_d.get('ApplicationID'),
            })
        result = {'result': resp.get('result'),'data': app_list}
        return render_json(result)