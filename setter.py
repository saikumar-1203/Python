class book:
  def set_bname(self,bname):
    self.bname=bname
  def set_aname(self,aname):
    self.aname=aname
  def set_cost(self,cost):
    self.cost=cost
  def set_pages(self,np):
    self.np=np
  def get_bname(self):
    return self.bname
  def get_aname(self):
    return self.aname
  def get_cost(self):
    return self.cost
  def get_np(self):
    return self.np
b1=book()
b1.set_bname("Python")
b1.set_aname("Guido")
b1.set_cost(500)
b1.set_pages(250)
print(b1.get_bname())
print(b1.get_aname())
print(b1.get_cost())
print(b1.get_np())