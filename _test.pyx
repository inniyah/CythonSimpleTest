# cython: profile=False
# cython: embedsignature = True
# cython: language_level = 3
# distutils: language = c++

# C-Import Cython Definitions

from libc.stdint cimport uint64_t, uint32_t, uint16_t, uint8_t
from libc.stdlib cimport calloc, malloc, free
from libc.string cimport memset, strcmp
from libc.stdio cimport printf

from libcpp cimport bool
from libcpp.memory cimport unique_ptr, shared_ptr, make_shared, allocator
from libcpp.string cimport string
from libcpp.vector cimport vector
from libcpp.utility cimport pair

from cpython cimport array
from cpython.ref cimport PyObject
from cpython.mem cimport PyMem_Malloc, PyMem_Realloc, PyMem_Free
from cpython.bytes cimport PyBytes_FromStringAndSize

from cython.operator cimport dereference as deref

from enum import IntEnum

# Import Python Modules

import array
import numbers

# C-Import Custom Cython Definitions

cimport example


def init():
    example.initStuff()

def destroy():
    example.destroyStuff()

def setGlobalName(name : str):
    example.setGlobalName(name.encode('utf8'))

def getGlobalName():
    return example.getGlobalName().decode('utf8')

def getGlobalBuffer():
    cdef size_t size
    cdef const char * buffer = <char *>example.getGlobalBuffer(&size)
    return PyBytes_FromStringAndSize(buffer, size)

def setGlobalBuffer(buffer : bytes):
    cdef const char * pbuffer = buffer
    example.setGlobalBuffer(<const uint8_t *>pbuffer, len(buffer))

# Gimmick Class

cdef class _gimmick:
    cdef example.Gimmick * _this

    def __cinit__(self):
        self._this = NULL

    def __dealloc___(self):
        self.destroy()

    def create(self):
        self.destroy()
        self._this = new example.Gimmick()

    def destroy(self):
        if self._this == NULL:
            del self._this

    def setName(self, name : str):
        self._this.setName(name.encode('utf8'))

    def getName(self):
        return self._this.getName().decode('utf8')

    def setBuffer(self, buffer : bytes):
        self._this.setBuffer(buffer)

    def getBuffer(self):
        cdef vector[uint8_t] v = self._this.getBuffer()
        cdef size_t size = v.size()
        cdef const char * pbuffer = <char *>&v[0];
        return PyBytes_FromStringAndSize(pbuffer, size)

    def printBuffer(self):
        buffer = self._this.getBuffer()
        print(":".join("{:02x}".format(c) for c in buffer))

    @property
    def counter(self):
        return self._this.counter
    @counter.setter
    def counter(self, counter : int):
        self._this.counter = counter
    DIR_UP = example.Gimmick.Direction.DIR_UP
    DIR_DOWN = example.Gimmick.Direction.DIR_DOWN
    def moveCounter(self, dir : int):
        return self._this.moveCounter(dir)

class Gimmick(_gimmick):
    def __init__(self):
        self.create()

