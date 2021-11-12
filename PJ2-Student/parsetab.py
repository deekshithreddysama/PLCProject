
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\xba\\\x155i\x0b\xe0BG\x1b\xd44\xce.85'
    
_lr_action_items = {'int':([0,17,50,80,81,85,],[5,5,5,5,5,5,]),'ob':([0,17,50,80,81,85,],[6,6,6,6,6,6,]),'proc':([0,17,50,80,81,85,],[7,7,7,7,7,7,]),'class':([0,17,50,80,81,85,],[8,8,8,8,8,8,]),'override':([0,17,50,80,81,85,],[9,9,9,9,9,9,]),'if':([0,2,4,17,23,34,46,75,80,81,87,88,],[-36,14,-3,-36,14,-2,14,14,-36,-36,14,14,]),'print':([0,2,4,17,23,34,46,75,80,81,87,88,],[-36,15,-3,-36,15,-2,15,15,-36,-36,15,15,]),'ID':([0,2,4,5,6,7,8,9,14,15,17,23,24,25,26,29,31,34,35,36,37,38,39,46,49,61,64,65,66,70,75,80,81,87,88,],[-36,16,-3,18,19,20,21,22,16,16,-36,16,16,16,45,16,16,-2,16,16,54,16,54,16,16,16,16,-32,-33,79,16,-36,-36,16,16,]),'$end':([0,1,2,4,10,11,12,16,17,23,28,30,32,33,34,40,41,45,48,51,59,78,84,89,93,],[-36,0,-36,-3,-1,-12,-14,-34,-36,-36,-27,-29,-31,-17,-2,-13,-15,-35,-30,-11,-18,-10,-28,-16,-9,]),';':([3,11,16,28,30,32,33,41,45,48,51,52,53,57,59,78,84,89,93,94,95,],[17,23,-34,-27,-29,-31,-17,-15,-35,-30,-11,-4,-5,-7,-18,-10,-28,-16,-9,-6,-8,]),'}':([4,17,34,50,68,85,90,],[-3,-36,-2,-36,78,-36,93,]),'end':([4,11,12,16,17,23,28,30,32,33,34,40,41,45,48,51,59,75,78,80,81,83,84,87,88,89,91,92,93,],[-3,-12,-14,-34,-36,-36,-27,-29,-31,-17,-2,-13,-15,-35,-30,-11,-18,-36,-10,-36,-36,89,-28,-36,-36,-16,94,95,-9,]),'else':([11,12,16,23,28,30,32,33,40,41,45,46,48,51,59,63,78,84,89,93,],[-12,-14,-34,-36,-27,-29,-31,-17,-13,-15,-35,-36,-30,-11,-18,75,-10,-28,-16,-9,]),'=':([13,16,18,19,45,],[24,-34,35,36,-35,]),'(':([13,14,15,16,20,22,24,25,29,35,36,45,61,64,65,66,],[25,29,29,-34,37,39,29,29,29,29,29,-35,29,29,-32,-33,]),'.':([13,16,30,45,51,],[26,-34,26,-35,26,]),'NUM':([14,15,24,25,29,35,36,61,64,65,66,],[28,28,28,28,28,28,28,28,28,-32,-33,]),'new':([14,15,24,25,29,35,36,61,64,65,66,],[31,31,31,31,31,31,31,31,31,-32,-33,]),'nil':([14,15,24,25,29,35,36,61,64,65,66,],[32,32,32,32,32,32,32,32,32,-32,-33,]),':':([16,21,27,28,30,32,45,48,51,72,73,78,84,93,],[-34,38,46,-27,-29,-31,-35,-30,-11,80,81,-10,-28,-9,]),',':([16,28,30,32,43,45,48,51,54,74,78,79,84,93,],[-34,-27,-29,-31,61,-35,-30,-11,70,61,-10,70,-28,-9,]),')':([16,25,28,30,32,37,39,42,43,44,45,48,51,54,55,56,58,60,62,69,71,74,76,78,79,82,84,86,93,],[-34,-36,-27,-29,-31,-36,-36,59,-36,-20,-35,-30,-11,-36,72,-24,73,-19,-22,-23,-26,-36,84,-10,-36,-21,-28,-25,-9,]),'+':([16,28,30,32,45,47,48,51,78,84,93,],[-34,-27,-29,-31,-35,65,-30,-11,-10,-28,-9,]),'-':([16,28,30,32,45,47,48,51,78,84,93,],[-34,-27,-29,-31,-35,66,-30,-11,-10,-28,-9,]),'with':([16,45,51,67,78,93,],[-34,-35,-11,77,-10,-9,]),'extend':([31,38,49,],[49,49,49,]),'{':([31,38,49,77,],[50,50,50,85,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'DeclarationList':([0,17,50,80,81,85,],[2,34,68,87,88,90,]),'Declaration':([0,17,50,80,81,85,],[3,3,3,3,3,3,]),'empty':([0,2,17,23,25,37,39,43,46,50,54,74,75,79,80,81,85,87,88,],[4,12,4,12,44,56,56,62,12,4,71,62,12,71,4,4,4,12,12,]),'CommandList':([2,23,46,75,87,88,],[10,40,63,83,91,92,]),'Command':([2,23,46,75,87,88,],[11,11,11,11,11,11,]),'LefthandSide':([2,14,15,23,24,25,29,31,35,36,38,46,49,61,64,75,87,88,],[13,30,30,13,30,30,30,51,30,30,51,13,51,30,30,13,13,13,]),'Expression':([14,15,24,25,29,35,36,61,64,],[27,33,41,43,47,52,53,74,76,]),'ExpressionList':([25,],[42,]),'TypeTemplate':([31,38,49,],[48,57,67,]),'IdentifierList':([37,39,],[55,58,]),'EListTail':([43,74,],[60,82,]),'Op':([47,],[64,]),'IListTail':([54,79,],[69,86,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('Program -> DeclarationList CommandList','Program',2,'p_Program','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',104),
  ('DeclarationList -> Declaration ; DeclarationList','DeclarationList',3,'p_DeclarationList1','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',111),
  ('DeclarationList -> empty','DeclarationList',1,'p_DeclarationList2','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',115),
  ('Declaration -> int ID = Expression','Declaration',4,'p_Declaration1','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',125),
  ('Declaration -> ob ID = Expression','Declaration',4,'p_Declaration2','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',129),
  ('Declaration -> proc ID ( IdentifierList ) : DeclarationList CommandList end','Declaration',9,'p_Declaration4','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',139),
  ('Declaration -> class ID : TypeTemplate','Declaration',4,'p_Declaration5','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',143),
  ('Declaration -> override ID ( IdentifierList ) : DeclarationList CommandList end','Declaration',9,'p_Declaration6','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',147),
  ('TypeTemplate -> extend TypeTemplate with { DeclarationList }','TypeTemplate',6,'p_TypeTemplate1','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',154),
  ('TypeTemplate -> { DeclarationList }','TypeTemplate',3,'p_TypeTemplate2','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',158),
  ('TypeTemplate -> LefthandSide','TypeTemplate',1,'p_TypeTemplate3','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',162),
  ('CommandList -> Command','CommandList',1,'p_CommandList','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',170),
  ('CommandList -> Command ; CommandList','CommandList',3,'p_CommandList','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',171),
  ('CommandList -> empty','CommandList',1,'p_CommandList','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',172),
  ('Command -> LefthandSide = Expression','Command',3,'p_Command1','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',186),
  ('Command -> if Expression : CommandList else CommandList end','Command',7,'p_Command2','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',190),
  ('Command -> print Expression','Command',2,'p_Command3','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',194),
  ('Command -> LefthandSide ( ExpressionList )','Command',4,'p_Command4','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',198),
  ('ExpressionList -> Expression EListTail','ExpressionList',2,'p_ExpressionList1','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',206),
  ('ExpressionList -> empty','ExpressionList',1,'p_ExpressionList2','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',210),
  ('EListTail -> , Expression EListTail','EListTail',3,'p_EListTail1','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',214),
  ('EListTail -> empty','EListTail',1,'p_EListTail2','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',218),
  ('IdentifierList -> ID IListTail','IdentifierList',2,'p_IdentifierList1','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',227),
  ('IdentifierList -> empty','IdentifierList',1,'p_IdentifierList2','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',231),
  ('IListTail -> , ID IListTail','IListTail',3,'p_IListTail1','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',235),
  ('IListTail -> empty','IListTail',1,'p_IListTail2','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',239),
  ('Expression -> NUM','Expression',1,'p_Expression1','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',250),
  ('Expression -> ( Expression Op Expression )','Expression',5,'p_Expression2','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',254),
  ('Expression -> LefthandSide','Expression',1,'p_Expression3','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',258),
  ('Expression -> new TypeTemplate','Expression',2,'p_Expression4','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',262),
  ('Expression -> nil','Expression',1,'p_Expression5','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',266),
  ('Op -> +','Op',1,'p_op1','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',271),
  ('Op -> -','Op',1,'p_op2','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',275),
  ('LefthandSide -> ID','LefthandSide',1,'p_LefthandSide1','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',282),
  ('LefthandSide -> LefthandSide . ID','LefthandSide',3,'p_LefthandSide2','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',286),
  ('empty -> <empty>','empty',0,'p_empty','/Users/hongmin/Documents/0-Teaching/CS311-HM/programming_assignment/PJ2-Student/a23pars.py',293),
]