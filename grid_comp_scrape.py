from jenkinsapi.jenkins \
	import Jenkins

def get_server_instance():
    jenkins_url = 'http://jenkins_host:8080'
    server = Jenkins(jenkins_url, username='foouser', password='foopassword')
    return server

if __name__ == '__main__':
    print get_server_instance().version