import email, wave 
msg = email.message_from_file(open('mission19.txt'))
for item in msg.get_payload():
    print item.get_payload(decode=True)
    if not item.is_multipart():
        open('indian.wav','wb').write(item.get_payload(decode=True))

old = wave.open('indian.wav','r')
new = wave.open('new.wav','w')
new.setparams(old.getparams())
for i in range(old.getnframes()):
    new.writeframes(old.readframes(1)[::-1])
new.close()