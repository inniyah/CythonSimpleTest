#pragma once

#ifndef GIMMICK_H_7FBFC2EA_6BEA_11ED_B0C7_3B6751BCFE99
#define GIMMICK_H_7FBFC2EA_6BEA_11ED_B0C7_3B6751BCFE99

#include <cstdint>
#include <string>
#include <vector>

namespace example {

class Gimmick {
public:
	Gimmick();
	Gimmick(const std::string & name);
	virtual ~Gimmick();

	void setName(const std::string & name);
	const std::string getName(void) const;
	void setBuffer(const std::vector<uint8_t> & buffer);
	const std::vector<uint8_t> & getBuffer(void) const;

	typedef int Counter;
	Counter counter = 0;
	enum Direction {
		DIR_UP,
		DIR_DOWN
	};
	Counter moveCounter(Direction dir);

private:
	std::string m_name;
	std::vector<uint8_t> m_buffer;
};

} // namespace example

#endif // GIMMICK_H_7FBFC2EA_6BEA_11ED_B0C7_3B6751BCFE99
