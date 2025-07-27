import requests


pixela_endpoint="https://pixe.la/v1/users"
username="adwaitdeshmukh"
token="adwaitnitinpallavi"
user_params={
    "token":"adwaitnitinpallavi",
    "username":"adwaitdeshmukh",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.json())

graph_endpoint=f"{pixela_endpoint}/{username}/graphs"
graph_config={
    "id":"graph1",
    "name":"coding graph",
    "unit":"programs ",
    "type":"int",
    "color":"sora"
}
headers={
    "X-USER-TOKEN":token
}
response_graph=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
print(response_graph.text)
