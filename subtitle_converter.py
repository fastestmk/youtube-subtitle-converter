import glob


def convert_youtube_subtitle_to_srt(youtube_subtitles_filename):
    base_filename = youtube_subtitles_filename.split('.')[0] #removing . from new.txt and accessing "new"
    srt_out_filename = '%s.srt' % base_filename # output filename is "new.srt"
    subtitles = list()
    with open(youtube_subtitles_filename, 'r') as infile:
        lines = infile.readlines()
        previous = None
        for index, line in enumerate(lines):
            #print(line) # printing line with gaps 
            text = ' '.join(line.split()) # joining lines with no gap
            # print(text)
            if index % 2 == 0: 
                entry = {'start_time': text}
                # print(entry)
                if previous is not None:
                    previous['end_time'] = text # getting first "start time" then subtitle then "end time" in entry
                    # print(previous)
            else:
                entry['subtitle'] = text  # adding subtitle after starting time in oddth iteration
                # print(entry)  #print(previous)
                subtitles.append(entry) # appeding entry and previous because previous = entry
                # print(subtitles)
                previous = entry # previous and entry dict() both are same i.e previous = &entry
                # print(previous) 
        if previous is not None:
            previous['end_time'] = previous['start_time']

    with open(srt_out_filename, 'w') as outfile:
        for index, entry in enumerate(subtitles):
            outfile.write('{0}\n'.format(index + 1))
            outfile.write('00:{0},000 --> 00:{1},000\n'.format(entry['start_time'], entry['end_time']))
            outfile.write('{0}\n'.format(entry['subtitle']))
            outfile.write('\n')


def main():
    files = glob.glob('*.txt')
    for filename in files: # for multiple subtitles
        convert_youtube_subtitle_to_srt(filename)


if __name__ == '__main__':
    main()