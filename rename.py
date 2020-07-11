

import os
import time
import sys


fileTypeList = ['jpg', 'JPG', 'mp4', 'MP4']


class CBatchRename():
	'''
	批量重命名文件夹中的图片文件
	'''
	def __init__(self, path = 'D:\\download\\test相册'):
		self.path = path

	def rename(self):
		filelist = os.listdir(self.path)
		total_num = len(filelist)
		for item in filelist:
			for fileType in fileTypeList:
				if item.endswith(fileType):
					src = os.path.join(os.path.abspath(self.path), item)
					dst = os.path.join(os.path.abspath(self.path), str(time.time()) + '_' + item)
					try:
						os.rename(src, dst)
						# print('converting', src, ' to ' ,dst)
					except:
						print('convert error', src, ' to ' ,dst )
						return
	
		filelist = os.listdir(self.path)
		total_num = len(filelist)
		i = 1
		for item in filelist:
			if item.endswith('.jpg') or item.endswith('.JPG'):
				src = os.path.join(os.path.abspath(self.path), item)
				dst = os.path.join(os.path.abspath(self.path), str(i) + '.jpg')
				try:
					os.rename(src, dst)
					# print('converting', src, ' to ', dst)
					i = i + 1
				except:
					print('convert error', src, ' to ', dst)
					return
		print('total ', total_num, ' rename')


def main():
	if len(sys.argv) == 1:
		batchRename = CBatchRename()
	elif len(sys.argv) == 2:
		batchRename = CBatchRename(sys.argv[1])	
	else:
		print('path error')
		return

	batchRename.rename()


if __name__ == '__main__':
	main()
