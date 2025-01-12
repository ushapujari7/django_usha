from django.http import HttpResponse
def landing_page(request):
    return HttpResponse('''
    
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>First web application</title>
</head>
<body>
<div style="text_align:center">
<h1 style="color:red">SOUTH INDIAN TRIP</h1>
</div>



</body>
</html> 
    ''')
