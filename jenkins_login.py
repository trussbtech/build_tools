from jenkinsapi.jenkins	import Jenkins

server = jenkins.Jenkins('http://100.25.142.138:8080/', username='admin', password='rhouse11!')

jenkins_url = "http://100.25.142.138:8080"
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
