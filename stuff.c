#include "stuff.h"

#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

static char * global_name = NULL;

static uint8_t * global_buffer = NULL;
size_t global_buffer_size = 0;

void initStuff(void) {
	puts("[initStuff]");
	global_name = strdup("");
}

void destroyStuff(void) {
	puts("[destroyStuff]");
	if (global_name) {
		free(global_name);
	}
	if (global_buffer) {
		free(global_buffer);
	}
}

void setGlobalName(const char * name) {
	if (global_name) {
		free(global_name);
	}
	global_name = strdup(name);
}

const char * getGlobalName(void) {
	return global_name;
}

void setGlobalBuffer(const uint8_t * buffer, size_t size) {
	if (global_buffer) {
		free(global_buffer);
	}
	global_buffer = malloc(size);
	memcpy(global_buffer, buffer, size);
	global_buffer_size = size;
}

const uint8_t * getGlobalBuffer(size_t * p_size) {
	if (p_size) {
		*p_size = global_buffer_size;
	}
	return global_buffer;
}
