# -*- coding: utf-8 -*-

from odoo import models, fields, api




class ContactInherite(models.Model):
     _inherit = 'res.partner'

     father_name = fields.Char(string='fatcher name')
     mother_name = fields.Char(string='mother name')
     name_family = fields.Char(compute='_compute_name_family', string='name family')
     
     @api.depends('father_name',"mother_name")
     def _compute_name_family(self):
          for record in self:
               record.name_family=str(record.father_name)+" "+str(record.mother_name)
     

     
class Group(models.Model):
     _name = 'school.group'

     name = fields.Char(string='name of group',required=True)
     level = fields.Selection(string='Level', selection=[('first_year', 'First Year'), ('second_year', 'Secend Year'),])
     
class Student(models.Model):
     _name = 'school.student'

     name = fields.Many2one("res.partner",string=" student name",required=True,ondelete="cascade")
     group = fields.Many2one("school.group",string=" student name",required=True,ondelete="cascade")  
     bac_type = fields.Char(string='bacaluriat type')
        

class Teacher(models.Model):
     _name = 'school.teacher'

     name = fields.Many2one("res.partner",string=" teacher name",required=True,ondelete="cascade")
     specialite = fields.Char(string='specialite',required=False)


class Class(models.Model):
     _name = 'school.class'

     name = fields.Char(string='name of the class',required=True)
     number_houres = fields.Integer(string='number of houres',required=True)

class Session(models.Model):
     _name = 'school.session'

     name = fields.Char(string='name of the session',required=True)
     session_class = fields.Many2one('school.class', string='class name')
     start_session = fields.Date(string='the session start')
     end_session = fields.Date(string='the session end in')



class Mark(models.Model):
     _name = 'school.mark'

     name = fields.Char(string='name of the mark',required=True)
     student = fields.Many2one("school.student", string='student')
     mark = fields.Integer(string='mark of the student')
     
class Exam(models.Model):
     _name = 'school.exam'

     name = fields.Char(string='name of the exam',required=True)
     exam_class = fields.Many2one('school.class', string='class name')
     start_exam = fields.Date(string='the exam start')
     end_exam = fields.Date(string='the exam end in')
     students = fields.Many2many('school.mark', string='students')