/**
 * IBM (C) Copyright 2017 Apache License Version 2.0
 * http://www.apache.org/licenses/LICENSE-2.0
 */
#ifndef SMCLIUNDOCUMENTED_H_
#define SMCLIUNDOCUMENTED_H_

#include "wrapperutils.h"

int imageIPLDeviceQuery(int argC, char* argV[], struct _vmApiInternalContext* vmapiContextP);
int imagePerformanceQuery(int argC, char* argV[], struct _vmApiInternalContext* vmapiContextP);
int ipAddrGet(int argC, char* argV[], struct _vmApiInternalContext* vmapiContextP);
int queryAsychronousOperationDM(int argC, char* argV[], struct _vmApiInternalContext* vmapiContextP);
int systemInfoQuery(int argC, char* argV[], struct _vmApiInternalContext* vmapiContextP);
int systemIOQuery(int argC, char* argV[], struct _vmApiInternalContext* vmapiContextP);
int systemPerformanceInfoQuery(int argC, char* argV[], struct _vmApiInternalContext* vmapiContextP);
int virtualNetworkQueryLAN(int argC, char* argV[], struct _vmApiInternalContext* vmapiContextP);
int virtualNetworkQueryOSA(int argC, char* argV[], struct _vmApiInternalContext* vmapiContextP);
int virtualNetworkVswitchQueryIUOStats(int argC, char* argV[], struct _vmApiInternalContext* vmapiContextP);
int xCATCommandsIUO(int argC, char* argV[], struct _vmApiInternalContext* vmapiContextP);

#endif /* SMCLIUNDOCUMENTED_H_ */
