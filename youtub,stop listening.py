{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exception: \n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import speech_recognition as sr\n",
    "from gtts import gTTS\n",
    "import pyaudio\n",
    "import playsound\n",
    "import datetime\n",
    "import subprocess\n",
    "import wikipedia\n",
    "import smtplib\n",
    "import webbrowser as wb\n",
    "import time\n",
    "\n",
    "def speak(text):\n",
    "    tts = gTTS(text = text, lang=\"en-UK\")\n",
    "    filename = \"voice1.mp3\"\n",
    "    tts.save(filename)\n",
    "    playsound.playsound(filename)\n",
    "    os.remove(filename)\n",
    "def gudio():\n",
    "    r = sr.Recognizer()\n",
    "    with sr.Microphone() as source:\n",
    "        audio = r.listen(source)\n",
    "        said = \"\"\n",
    "\n",
    "        try:\n",
    "            said = r.recognize_google(audio)\n",
    "            print(said)\n",
    "        except Exception as lk:\n",
    "            print(\"Exception: \"+str(lk))\n",
    "    return said.lower()\n",
    "text = gudio()\n",
    "\n",
    "if 'open youtube and search' in text:\n",
    "    speak(\"What should I search?\")\n",
    "    text = text.replace(\"open youtube and search\",\"\")\n",
    "    Search_term = text\n",
    "    speak(\"Here we go to Youtube\\n\")\n",
    "    wb.open(\"https://www.youtube.com/results?search_query=\" + Search_term)\n",
    "    \n",
    "if 'play the song' in text:\n",
    "    text = text.replace('play the song',\"\")\n",
    "    Search_term = text\n",
    "    speak(\"Here we go to Youtube Music\\n\")\n",
    "    wb.open(\"https://music.youtube.com/search?q=\" + Search_term)\n",
    "    \n",
    "if \"don't listen\" in text or \"stop listening\" in text:\n",
    "    speak(\"for how much minutes you want me to stop listening commands\")\n",
    "    a = gudio()\n",
    "    time.sleep(int(a))\n",
    "    print(a)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
