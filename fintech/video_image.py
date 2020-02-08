# import cv2
# import os


# def sideways(username):
#     print("move your face sideways and press q when ready")
#     val =0
#     cap = cv2.VideoCapture(0)
#     dir = '/home/ekta/hack/'+username

#     current_frame = 100

#     while True:
#         ret,frame = cap.read()

#         cv2.imshow('frame',frame)

#         if cv2.waitKey(10) == ord('q'):
#             val = 1


#         if ret and val == 1:
#             if(current_frame%5==0):
#                 name = dir +'/' +str(username) + str(current_frame) +'.jpg'
#                 print("creating image"+name)


#             cv2.imwrite(name,frame)

#             current_frame +=1


#         if(current_frame==160):
#             break

#     cap.release()
#     cv2.destroyAllWindows()



# def front(username):
#     cap = cv2.VideoCapture(0)
#     dir = '/home/ekta/hack/'+username
#     try:
#         os.mkdir(dir)
#     except:
#         pass
#     current_frame =0

#     print("Adjust your face and press q to proceed for images")

#     val = 0
#     while True:
#         ret,frame = cap.read()
#         cv2.imshow('frame',frame)


#         if cv2.waitKey(10) == ord('q'):
#             val = 1

#         if ret and val == 1:
#             if(current_frame%5==0):
#                 name = dir +'/' +username + str(current_frame) +'.jpg'
#                 print("creating image"+name)


#             cv2.imwrite(name,frame)

#             current_frame +=1


#         if(current_frame==60):

#             cap.release()
#             cv2.destroyAllWindows()

#             # sideways(username)
#             break
