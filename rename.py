

import os
import time
import sys


fileTypeList = ['jpg', 'JPG', 'mp4', 'MP4']


'''
批量重命名文件夹中的图片文件
'''
class CBatchRename():
	def __init__(self, path = 'D:\\test', numLen = '5', prefix = ''):
		self.path = path
		self.numLen = int(numLen)
		if self.numLen < 3:
			self.numLen = 3
		if 5 < self.numLen:
			self.numLen = 5
		self.prefix = prefix

	def Rename(self):
		if not os.path.exists(self.path):
			print('path error', self.path)
			return

		# 避免当前名字和改后名字重名 统一修改成独特名字
		filelist = os.listdir(self.path)
		for item in filelist:
			for fileType in fileTypeList:
				if item.endswith(fileType):
					src = os.path.join(os.path.abspath(self.path), item)
					dst = os.path.join(os.path.abspath(self.path), str(time.time()) + '_' + item)
					try:
						os.rename(src, dst)
						# print('converting', src, ' to ', dst)
					except:
						print('convert error', src, ' to ', dst)
						return
	
		filelist = os.listdir(self.path)
		total_num = len(filelist)
		i = 1
		for item in filelist:
			for fileType in fileTypeList:
				if item.endswith(fileType):
					src = os.path.join(os.path.abspath(self.path), item)
					dst = os.path.join(os.path.abspath(self.path), \
						self.GetPrefix() + self.GetNum(i) + '.' + fileType)
					try:
						os.rename(src, dst)
						# print('converting', src, ' to ', dst)
						i = i + 1
					except:
						print('convert error', src, ' to ', dst)
						return			
		print('total ', total_num, ' rename')
	

	def GetPrefix(self):
		if self.prefix == '':
			return ''
		ret = ''
		ret = self.prefix + '_'
		return ret
	
	def GetNum(self, num):
		numStr = str(num)
		ret = numStr.zfill(self.numLen)
		return ret


def main():
	if len(sys.argv) == 1:
		batchRename = CBatchRename()
	elif len(sys.argv) == 2:
		batchRename = CBatchRename(sys.argv[1])
	elif len(sys.argv) == 3:
		batchRename = CBatchRename(sys.argv[1], sys.argv[2])
	elif len(sys.argv) == 4:
		batchRename = CBatchRename(sys.argv[1], sys.argv[2], sys.argv[3])
	else:
		print('arg num error')
		return
	batchRename.Rename()


if __name__ == '__main__':
	main()

