from socket import *
import ssl
import base64

msg = "\r\n I love Computer Networks"
endmsg = "\r\n.\r\n"

mailserver = ("smtp.gmail.com", 587) 

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

secureConnect = 'STARTTLS\r\n'.encode()
clientSocket.send(secureConnect)
recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':
    print ('220 reply not received from server')

#Encrypt the socket
clientSocket = ssl.wrap_socket(clientSocket)

# Info for username and password
email = (base64.b64encode('h.mashawn2@gmail.com'.encode())+('\r\n').encode())
password = (base64.b64encode('Cannucks2333!'.encode())+('\r\n').encode())
clientSocket.send('AUTH LOGIN \r\n'.encode())
recv_auth = clientSocket.recv(1024).decode()
print(recv_auth)
if recv_auth[:3] != '334':
    print('334 reply not received from server.')

clientSocket.send(email)
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '334':
    print ('334 reply not received from server')

clientSocket.send(password)
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '235':
    print ('235 reply not received from server')

# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <h.mashawn2@gmail.com> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptTo = "RCPT TO: <h.mashawn2@gmail.com>\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
subject = "Subject: Test Message from SMTP\r\n\r\n" 
clientSocket.send(subject.encode())
message = raw_input("Enter your message: \r\n")
clientSocket.send(message.encode())
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024)
print(recv_msg)
if recv_msg[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode())
message=clientSocket.recv(1024)
print (message)
clientSocket.close()