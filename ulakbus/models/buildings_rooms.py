# -*-  coding: utf-8 -*-
"""
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from pyoko import field, Model

__author__ = 'Ali Riza Keles'


class Campus(Model):
    code = field.String("Code", index=True)
    name = field.String("Name", index=True)
    coordinate_x = field.String("Coordinate X", index=True)
    coordinate_y = field.String("Coordinate Y", index=True)

    class Meta:
        verbose_name = "Campus"
        verbose_name_plural = "Campuses"
        search_fields = ['code', 'name']
        list_fields = ['code', 'name']

    def __unicode__(self):
        return '%s %s %s' % (self.code, self.name, self.coordinates())

    def coordinates(self):
        return '%s %s' % (self.coordinate_x, self.coordinate_y)


class Building(Model):
    code = field.String("Code", index=True)
    name = field.String("Name", index=True)
    coordinate_x = field.String("Coordinate X", index=True)
    coordinate_y = field.String("Coordinate Y", index=True)
    campus = Campus()

    class Meta:
        verbose_name = "Building"
        verbose_name_plural = "Buildings"
        search_fields = ['code', 'name', 'campus']
        list_fields = ['code', 'name', 'campus']

    def __unicode__(self):
        return '%s %s %s %s' % (self.code, self.name, self.coordinates(), self.campus)

    def coordinates(self):
        return '%s %s' % (self.coordinate_x, self.coordinate_y)


class RoomType(Model):
    type = field.String("Room Type", index=True)
    notes = field.Text("Notes", index=True)

    def __unicode__(self):
        return '%s %s %s' % (self.type)


class Room(Model):
    code = field.String("Code", index=True)
    name = field.String("Name", index=True)
    room_type = RoomType("Room Type", index=True)
    floor = field.String("Floor", index=True)
    capacity = field.Integer("Capacity", index=True)
    building = Building()
    is_active = field.Boolean("Active", index=True)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        search_fields = ['code', 'name', 'building']
        list_fields = ['code', 'name', 'building']

    def __unicode__(self):
        return '%s %s %s' % (self.code, self.name, self.capacity)