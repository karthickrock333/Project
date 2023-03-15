import cv2
import pytesseract
import csv

image_path=r'C:\Users\DELL\Desktop\Roi\M4.png'
CSV_file='C:/Users/DELL/Desktop/Roi/RAMA.csv'

roi2=[[(38, 136), (192, 190), 'text', 'Address'],
     [(509, 86), (617, 114), 'text', 'No'],
     [(629, 85), (712, 112), 'text', 'Date'],
     [(512, 140), (616, 164), 'text', 'Payment Methord'],
     [(643, 140), (712, 164), 'text', 'Amount'],
     [(127, 190), (204, 207), 'text', 'For'],
     [(128, 216), (566, 244), 'text', 'Recived By']]

roi=[[(43, 134), (217, 223), 'text', 'Address'],
     [(38, 253), (196, 327), 'text', 'BillTo'],
     [(257, 254), (433, 329), 'text', 'Ship to '],
     [(596, 231), (718, 261), 'text', 'Recipt#'],
     [(624, 258), (704, 281), 'text', 'Recpit Data'],
     [(621, 284), (707, 311), 'text', 'P.O.#'],
     [(623, 315), (705, 336), 'text', 'Due Date'],
     [(543, 380), (706, 423), 'text', 'Recipt Total'],
     [(33, 505), (89, 591), 'text', 'Qty'],
     [(118, 509), (403, 602), 'text', 'Description'],
     [(446, 499), (565, 611), 'text', 'Unit Price'],
     [(625, 499), (726, 597), 'text', 'Amount'],
     [(617, 607), (731, 636), 'text', 'SubTotal'],
     [(492, 637), (717, 665), 'non', 'non'],
     [(493, 634), (545, 664), 'text', 'Sale Tax%'],
     [(632, 634), (729, 669), 'text', 'SaleTax Amount']]

roi3=[[(272, 200), (472, 234), 'text', 'Refer NO'],
     [(270, 244), (502, 280), 'text', 'Transfer To'],
     [(270, 284), (458, 318), 'text', 'Account Type'],
     [(270, 326), (510, 370), 'text', 'Account No'],
     [(270, 368), (510, 400), 'text', 'Account Name'],
     [(268, 408), (498, 446), 'text', 'Transfer From '],
     [(266, 448), (500, 486), 'text', 'Amount'],
     [(266, 488), (494, 528), 'text', 'Transfer When'],
     [(264, 528), (622, 594), 'text', 'Puropse']]

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread(image_path)


with open(CSV_file, 'w', newline='') as f:
    writer = csv.writer(f)

    # Write header rows
    header_row = [r[3] for r in roi if r[2] == 'text']
    writer.writerow(header_row)

    # Loop over the ROIs and extract the texts
    extracted_data = []
    for r in roi:
        imgcrop = img[r[0][1]:r[1][1],r[0][0]:r[1][0]]
        if r[2] == 'text':
            extracted_text = pytesseract.image_to_string(imgcrop).strip()
            extracted_data.append(extracted_text)
            print(f'{r[3]}: {extracted_text}')
    writer.writerow(extracted_data)