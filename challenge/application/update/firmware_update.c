#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int main(void)
{
	setuid(0);
        system("/bin/bash ./firmware_update.sh");
}
