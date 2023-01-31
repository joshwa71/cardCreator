import os
import zipfile

if __name__ == '__main__':
    extract = r"C:\Users\joshu\Documents\Biz\CardCreator\Orders"
    zips_dir = r"C:\Users\joshu\Documents\Biz\CardCreator\zips"
    zips = os.listdir(r"C:\Users\joshu\Documents\Biz\CardCreator\zips")
    orders_dir = os.listdir(r"C:\Users\joshu\Documents\Biz\CardCreator\Orders")
    i = 1
    for order in zips:
        order_name = order[:-4]
        print(order_name)
        zip_path = zips_dir + '/' + order
        extract_path = extract + '/' + order_name
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        i += 1