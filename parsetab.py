
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA FALSE ID IGUAL LCHAV LESS LPAREN NUMBER POT PV RCHAV RETURN RPAREN SOMA TRUE VEZES WHILEprogram : funcdeclprogram : funcdecl programprogram : globalvardecl programprogram : globalvardeclprogram : callglobalprogram : callglobal programglobalvardecl : ID IGUAL expless PVcallglobal : call PVfuncdecl : signature bodysignature : ID ID LPAREN sigparams RPARENsignature : ID ID LPAREN RPARENsigparams : ID IDsigparams :  ID ID COMMA sigparams body : LCHAV stms RCHAV body : LCHAV RCHAV stms : stm stms : stm stms stm :  exp PV stm :  WHILE LPAREN exp RPAREN body stm :  RETURN exp PV exp :    exp IGUAL expless exp : explessexpless : expless LESS exp1expless : exp1exp1 : exp1 SOMA exp2exp1 : exp2exp2 : exp2 VEZES exp3exp2 : exp3exp3 : exp4 POT exp3exp3 : exp4exp4 : callexp4 : NUMBERexp4 : IDexp4 : TRUE\n            | FALSEcall : ID LPAREN params RPARENcall : ID LPAREN RPARENparams : exp COMMA params params : exp '
    
_lr_action_items = {'ID':([0,2,3,4,6,11,12,14,15,16,18,19,22,33,38,40,41,42,44,45,46,47,48,51,53,56,65,66,],[6,6,6,6,13,-9,30,30,30,-8,-15,30,30,48,-14,-18,30,30,30,30,30,30,61,-7,30,-20,48,-19,]),'$end':([1,2,3,4,8,9,10,11,16,18,38,51,],[0,-1,-4,-5,-2,-3,-6,-9,-8,-15,-14,-7,]),'LCHAV':([5,50,62,64,],[12,-11,-10,12,]),'IGUAL':([6,20,23,24,25,26,27,28,29,30,31,32,36,37,43,52,54,55,57,58,59,60,],[14,41,-22,-24,-26,-28,-30,-31,-32,-33,-34,-35,-37,41,41,-36,-21,41,-23,-25,-27,-29,]),'LPAREN':([6,13,21,30,],[15,33,42,15,]),'PV':([7,20,23,24,25,26,27,28,29,30,31,32,34,36,43,52,54,57,58,59,60,],[16,40,-22,-24,-26,-28,-30,-31,-32,-33,-34,-35,51,-37,56,-36,-21,-23,-25,-27,-29,]),'RCHAV':([12,17,18,19,38,39,40,56,66,],[18,38,-15,-16,-14,-17,-18,-20,-19,]),'WHILE':([12,18,19,38,40,56,66,],[21,-15,21,-14,-18,-20,-19,]),'RETURN':([12,18,19,38,40,56,66,],[22,-15,22,-14,-18,-20,-19,]),'NUMBER':([12,14,15,18,19,22,38,40,41,42,44,45,46,47,53,56,66,],[29,29,29,-15,29,29,-14,-18,29,29,29,29,29,29,29,-20,-19,]),'TRUE':([12,14,15,18,19,22,38,40,41,42,44,45,46,47,53,56,66,],[31,31,31,-15,31,31,-14,-18,31,31,31,31,31,31,31,-20,-19,]),'FALSE':([12,14,15,18,19,22,38,40,41,42,44,45,46,47,53,56,66,],[32,32,32,-15,32,32,-14,-18,32,32,32,32,32,32,32,-20,-19,]),'RPAREN':([15,23,24,25,26,27,28,29,30,31,32,33,35,36,37,49,52,54,55,57,58,59,60,61,63,67,],[36,-22,-24,-26,-28,-30,-31,-32,-33,-34,-35,50,52,-37,-39,62,-36,-21,64,-23,-25,-27,-29,-12,-38,-13,]),'COMMA':([23,24,25,26,27,28,29,30,31,32,36,37,52,54,57,58,59,60,61,],[-22,-24,-26,-28,-30,-31,-32,-33,-34,-35,-37,53,-36,-21,-23,-25,-27,-29,65,]),'LESS':([23,24,25,26,27,28,29,30,31,32,34,36,52,54,57,58,59,60,],[44,-24,-26,-28,-30,-31,-32,-33,-34,-35,44,-37,-36,44,-23,-25,-27,-29,]),'SOMA':([24,25,26,27,28,29,30,31,32,36,52,57,58,59,60,],[45,-26,-28,-30,-31,-32,-33,-34,-35,-37,-36,45,-25,-27,-29,]),'VEZES':([25,26,27,28,29,30,31,32,36,52,58,59,60,],[46,-28,-30,-31,-32,-33,-34,-35,-37,-36,46,-27,-29,]),'POT':([27,28,29,30,31,32,36,52,],[47,-31,-32,-33,-34,-35,-37,-36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,2,3,4,],[1,8,9,10,]),'funcdecl':([0,2,3,4,],[2,2,2,2,]),'globalvardecl':([0,2,3,4,],[3,3,3,3,]),'callglobal':([0,2,3,4,],[4,4,4,4,]),'signature':([0,2,3,4,],[5,5,5,5,]),'call':([0,2,3,4,12,14,15,19,22,41,42,44,45,46,47,53,],[7,7,7,7,28,28,28,28,28,28,28,28,28,28,28,28,]),'body':([5,64,],[11,66,]),'stms':([12,19,],[17,39,]),'stm':([12,19,],[19,19,]),'exp':([12,15,19,22,42,53,],[20,37,20,43,55,37,]),'expless':([12,14,15,19,22,41,42,53,],[23,34,23,23,23,54,23,23,]),'exp1':([12,14,15,19,22,41,42,44,53,],[24,24,24,24,24,24,24,57,24,]),'exp2':([12,14,15,19,22,41,42,44,45,53,],[25,25,25,25,25,25,25,25,58,25,]),'exp3':([12,14,15,19,22,41,42,44,45,46,47,53,],[26,26,26,26,26,26,26,26,26,59,60,26,]),'exp4':([12,14,15,19,22,41,42,44,45,46,47,53,],[27,27,27,27,27,27,27,27,27,27,27,27,]),'params':([15,53,],[35,63,]),'sigparams':([33,65,],[49,67,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> funcdecl','program',1,'p_program1','ExpressionLanguageParser.py',19),
  ('program -> funcdecl program','program',2,'p_program2','ExpressionLanguageParser.py',23),
  ('program -> globalvardecl program','program',2,'p_program3','ExpressionLanguageParser.py',27),
  ('program -> globalvardecl','program',1,'p_program4','ExpressionLanguageParser.py',31),
  ('program -> callglobal','program',1,'p_program5','ExpressionLanguageParser.py',35),
  ('program -> callglobal program','program',2,'p_program6','ExpressionLanguageParser.py',39),
  ('globalvardecl -> ID IGUAL expless PV','globalvardecl',4,'p_vardecl','ExpressionLanguageParser.py',43),
  ('callglobal -> call PV','callglobal',2,'p_callglobal','ExpressionLanguageParser.py',47),
  ('funcdecl -> signature body','funcdecl',2,'p_funcdecl','ExpressionLanguageParser.py',51),
  ('signature -> ID ID LPAREN sigparams RPAREN','signature',5,'p_signature1','ExpressionLanguageParser.py',55),
  ('signature -> ID ID LPAREN RPAREN','signature',4,'p_signature2','ExpressionLanguageParser.py',60),
  ('sigparams -> ID ID','sigparams',2,'p_sigparams1','ExpressionLanguageParser.py',64),
  ('sigparams -> ID ID COMMA sigparams','sigparams',4,'p_sigparams2','ExpressionLanguageParser.py',68),
  ('body -> LCHAV stms RCHAV','body',3,'p_body1','ExpressionLanguageParser.py',72),
  ('body -> LCHAV RCHAV','body',2,'p_body2','ExpressionLanguageParser.py',76),
  ('stms -> stm','stms',1,'p_stms1','ExpressionLanguageParser.py',80),
  ('stms -> stm stms','stms',2,'p_stms2','ExpressionLanguageParser.py',84),
  ('stm -> exp PV','stm',2,'p_stm1','ExpressionLanguageParser.py',88),
  ('stm -> WHILE LPAREN exp RPAREN body','stm',5,'p_stm2','ExpressionLanguageParser.py',92),
  ('stm -> RETURN exp PV','stm',3,'p_stm3','ExpressionLanguageParser.py',96),
  ('exp -> exp IGUAL expless','exp',3,'p_exp_assign1','ExpressionLanguageParser.py',100),
  ('exp -> expless','exp',1,'p_exp_assign2','ExpressionLanguageParser.py',104),
  ('expless -> expless LESS exp1','expless',3,'p_exp_less1','ExpressionLanguageParser.py',108),
  ('expless -> exp1','expless',1,'p_exp_less2','ExpressionLanguageParser.py',112),
  ('exp1 -> exp1 SOMA exp2','exp1',3,'p_exp1_soma1','ExpressionLanguageParser.py',117),
  ('exp1 -> exp2','exp1',1,'p_exp1_soma2','ExpressionLanguageParser.py',121),
  ('exp2 -> exp2 VEZES exp3','exp2',3,'p_exp2_vezes1','ExpressionLanguageParser.py',125),
  ('exp2 -> exp3','exp2',1,'p_exp2_vezes2','ExpressionLanguageParser.py',129),
  ('exp3 -> exp4 POT exp3','exp3',3,'p_exp3_pot1','ExpressionLanguageParser.py',133),
  ('exp3 -> exp4','exp3',1,'p_exp3_pot2','ExpressionLanguageParser.py',137),
  ('exp4 -> call','exp4',1,'p_exp4_call1','ExpressionLanguageParser.py',141),
  ('exp4 -> NUMBER','exp4',1,'p_exp4_call2','ExpressionLanguageParser.py',145),
  ('exp4 -> ID','exp4',1,'p_exp4_call3','ExpressionLanguageParser.py',149),
  ('exp4 -> TRUE','exp4',1,'p_exp4_call4','ExpressionLanguageParser.py',154),
  ('exp4 -> FALSE','exp4',1,'p_exp4_call4','ExpressionLanguageParser.py',155),
  ('call -> ID LPAREN params RPAREN','call',4,'p_call_id_params1','ExpressionLanguageParser.py',159),
  ('call -> ID LPAREN RPAREN','call',3,'p_call_id_params2','ExpressionLanguageParser.py',164),
  ('params -> exp COMMA params','params',3,'p_params_ids1','ExpressionLanguageParser.py',169),
  ('params -> exp','params',1,'p_params_ids2','ExpressionLanguageParser.py',173),
]
