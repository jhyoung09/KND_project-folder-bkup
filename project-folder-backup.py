









#   imports
import datetime, zipfile, shutil, os
from filecmp import dircmp

#   global variable

kah_remote = r'C:\Users\youngj42\Desktop\folder2'
kah_local = r'C:\Users\youngj42\Desktop\folder1'




def date():
    date = datetime.datetime.now()
    return date.strftime('%d %m %Y')

def compare(kah_remote,kah_local,output,output_txt=True, output_csv=False):
    report = recursiveDIRCMP(kah_remote,kah_local)

    kah_remote = kah_remote.replace('\\', '/')
    kah_local = kah_local.replace('\\', '/')

    if output_txt:
        writePlainText(kah_remote, kah_local, output, report)

    if output_csv:
        writeCSV(kah_remote, kah_local, output, report)

def recursiveDIRCMP(kah_remote, kah_local):
    comparison = filecmp.dircmp(kah_remote,kah_local)

    date = {
        'left': [r'{}/{}'.format(prefix, i) for i in comparison.left_only],
        'right': [r'{}/{}'.format(prefix, i) for i in comparison.right_only],
        'both': [r'{}/{}'.format(prefix, i) for i in comparison.common_files],
    }

    for datalist in data.values():
        datalist.sort()

    if conparison.commonDIRS:
        for folder in comparison.commonDIRS:
            prefix += '/' + folder

            subFolder01 = os.path.join(kah_remote, folder)
            subFolder02 = os.path.join(kah_local, folder)
            subReport = recursiveDIRCMP(subFolder01, subFolder02, prefix)

            for key, value in subReport.items():
                data[key] += value
    return data


def writePlainText(kah_remote, kah_local, output, report):
    """Write the comparison report to a plain text file."""

    filename = output + '.txt'
    with open(filename, 'w') as file:
        file.write('COMPARISON OF FILES BETWEEN FOLDERS:\n')
        file.write('\tFOLDER 1: {}\n'.format(kah_remote))
        file.write('\tFOLDER 2: {}\n'.format(kah_local))
        file.write('\n\n')

        file.write('FILES ONLY IN: {}\n'.format(kah_remote))
        for item in report['left']:
            file.write('\t' + item + '\n')
        if not report['left']:
            file.write('\tNone\n')
        file.write('\n\n')

        file.write('FILES ONLY IN: {}\n'.format(kah_local))
        for item in report['right']:
            file.write('\t' + item + '\n')
        if not report['right']:
            file.write('\tNone\n')
        file.write('\n\n')

        file.write('FILES IN BOTH FOLDERS:\n')
        for item in report['both']:
            file.write('\t' + item + '\n')
        if not report['both']:
            file.write('\tNone\n')


def main():
    print(date())
    compare(kah_remote,kah_local,output,output_txt=True)
    print(recursiveDIRCMP)


main()