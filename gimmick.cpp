#include "gimmick.h"

namespace example {

Gimmick::Gimmick() {
}

Gimmick::Gimmick(const std::string & name) : m_name(name) {
}

Gimmick::~Gimmick() {
}

void Gimmick::setName(const std::string & name) {
	m_name = name;
}

const std::string Gimmick::getName(void) const {
	return m_name;
}

void Gimmick::setBuffer(const std::vector<uint8_t> & buffer) {
	m_buffer = buffer;
}

const std::vector<uint8_t> & Gimmick::getBuffer(void) const {
	return m_buffer;
}

Gimmick::Counter Gimmick::moveCounter(Gimmick::Direction dir) {
	switch (dir) {
		case Gimmick::DIR_UP:
			return ++counter;
			break;
		case Gimmick::DIR_DOWN:
			return --counter;
			break;
		default:
			return counter;
	}
}

} // namespace example
