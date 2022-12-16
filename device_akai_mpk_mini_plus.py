# name=Akai MPK Mini Plus
# url=https://github.com/abbydiode/fl-studio-akai-mpk-mini-plus-script

import general
import transport
import midi

BUTTON_PREVIOUS = 0x73
BUTTON_NEXT = 0x74
BUTTON_STOP = 0x75
BUTTON_PLAY = 0x76
BUTTON_RECORD = 0x77
SCRUB_TIME = 5

def OnControlChange(event):
    event.handled = False
    if event.data2 > 0:
        if event.data1 == BUTTON_PREVIOUS or event.data1 == BUTTON_NEXT:
            should_forward = event.data1 == BUTTON_NEXT
            new_song_pos = transport.getSongPos(midi.SONGLENGTH_S) + (SCRUB_TIME if should_forward else -SCRUB_TIME)
            print(f'{"Forwarding" if should_forward else "Rewinding"} {new_song_pos}/{transport.getSongLength(midi.SONGLENGTH_S)}')
            transport.setSongPos(new_song_pos, midi.SONGLENGTH_S)
        elif event.data1 == BUTTON_PLAY:
            print(f'{"Paused" if transport.isPlaying() else "Started"} playback')
            transport.start()
        elif event.data1 == BUTTON_STOP:
            print('Stopped playback')
            transport.stop()
        elif event.data1 == BUTTON_RECORD:
            print(f'{"Disabled" if transport.isRecording() else "Enabled"} recording')
            transport.record()
        event.handled = True