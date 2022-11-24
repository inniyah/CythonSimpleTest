#pragma once

#ifndef STUFF_H_41C38E46_6BEE_11ED_AFC3_6F1F7B2AA83F
#define STUFF_H_41C38E46_6BEE_11ED_AFC3_6F1F7B2AA83F

#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

void initStuff(void);

void destroyStuff(void);

void setGlobalName(const char * name);

const char * getGlobalName(void);

void setGlobalBuffer(const uint8_t * buffer, size_t size);

const uint8_t * getGlobalBuffer(size_t * p_size);

#ifdef __cplusplus
}
#endif

#endif // STUFF_H_41C38E46_6BEE_11ED_AFC3_6F1F7B2AA83F
