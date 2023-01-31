import cv2
import os

def concat_covers(directory, order):
    order_path = directory + "\Orders" + "/" + order
    covers_path = directory + "\Covers" + "/"
    print(order_path + order + ".1.jpeg")
    img1 = cv2.imread(order_path + '/' + order + ".1.jpeg")
    img2 = cv2.imread(order_path + '/' + order + ".4.jpeg")
    img = cv2.hconcat([img2, img1])

    # sr = cv2.dnn_superres.DnnSuperResImpl_create()
    # path = "EDSR_x4.pb"
    # sr.readModel(path)

    #sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    #sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

    # sr.setModel("edsr", 4)
    # result = sr.upsample(img)

    #orders_write = order_path + "/" + order + "covers.jpeg"
    #cv2.imwrite(orders_write, result

    covers_write = covers_path + "/" + order + ".jpeg"
    cv2.imwrite(covers_write, img)

def concat_insides(directory, order):
    order_path = directory + "\Orders" + "/" + order
    insides_path = directory + "\Insides" + "/"
    print(order_path + order + ".1.jpeg")
    img1 = cv2.imread(order_path + '/' + order + ".2.jpeg")
    img2 = cv2.imread(order_path + '/' + order + ".3.jpeg")
    img = cv2.hconcat([img1, img2])

    # sr = cv2.dnn_superres.DnnSuperResImpl_create()
    # path = "EDSR_x4.pb"
    # sr.readModel(path)

    #sr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    #sr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

    # sr.setModel("edsr", 4)
    # result = sr.upsample(img)

    #orders_write = order_path + "/" + order + "covers.jpeg"
    #cv2.imwrite(orders_write, result

    insides_write = insides_path + "/" + order + ".jpeg"
    cv2.imwrite(insides_write, img)

if __name__ == "__main__":
    directory = r"C:\Users\joshu\Documents\Biz\CardCreator"
    orders = os.listdir(r"C:\Users\joshu\Documents\Biz\CardCreator\Orders")
    print(orders)
    for order in orders:
        concat_covers(directory, order)
        concat_insides(directory, order)