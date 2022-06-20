import cv2

Num = 0
frame_total = 30
print(frame_total, Num)
while Num <= frame_total-1:
  # caculate the current frame
  # The width of the progress bar = (current frame /Total frame) * Width of the frame
  Width = int((( Num/frame_total)*420))
  Num +=1
  print(Num, frame_total, Width)
  # features for rectangle
  ptLeftTop = (0, 0)
  ptRightBottom = (Width, 20)
  point_color = (0, 0, 255) # BGR
  thickness = 20
  lineType = 8
  # frame
  ret,frame=cap.read()
  frame = cv2.resize(frame, (420,360), interpolation = cv2.INTER_AREA)
  frame = cv2.rectangle(frame, ptLeftTop, ptRightBottom, point_color, thickness, lineType)
  # cv2.imshow("video",frame)
  # 在播放每一帧时，使用cv2.waitKey()设置适当的持续时间。如果设置的太低视频就会播放的非常快，如果设置的太高就会播放的很慢。通常情况下25ms就ok
  if cv2.waitKey(25)&0xFF==ord('q'):
     cv2.destroyAllWindows()
     break

print("Mission Down")
