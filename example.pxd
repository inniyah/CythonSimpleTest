from libc.stdint cimport int32_t, uint32_t, int16_t, uint16_t, int8_t, uint8_t
from libcpp cimport bool
from libcpp.memory cimport unique_ptr, shared_ptr, allocator
from libcpp.string cimport string
from libcpp.vector cimport vector
from libcpp.map cimport map
from libcpp.unordered_map cimport unordered_map
from libcpp.utility cimport pair
from cpython.ref cimport PyObject

cdef extern from "stuff.h" nogil:
	void initStuff()
	void destroyStuff()
	void setGlobalName(const char * name)
	const char * getGlobalName()
	void setGlobalBuffer(const uint8_t * buffer, size_t size)
	const uint8_t * getGlobalBuffer(size_t * p_size)

cdef extern from "gimmick.h" namespace "example" nogil:
	cdef cppclass Gimmick:
		Gimmick() except +
		Gimmick(string) except +
		const void setName(string & name)
		const string getName() const
		const void setBuffer(const vector[uint8_t] & buffer)
		const vector[uint8_t] & getBuffer() const

		ctypedef int Counter
		Counter counter
		enum Direction:
			DIR_UP "::example::Gimmick::DIR_UP"
			DIR_DOWN "::example::Gimmick::DIR_DOWN"
		Counter moveCounter(Direction dir)
