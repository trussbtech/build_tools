import sys
import jenkins


server = jenkins.Jenkins('http://100.25.142.138:8080', username='admin', password='rhouse11')

output_text = server.get_build_console_output('Java-maven-HelloWorld', 11)

print("Successfully login")
print("")

output_lines = output_text.split('\n')
print(output_lines) 