# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.3
#
# <auto-generated>
#
# Generated from file `trawlnet.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module TrawlNet
_M_TrawlNet = Ice.openModule('TrawlNet')
__name__ = 'TrawlNet'

if 'FileDoesNotExistError' not in _M_TrawlNet.__dict__:
    _M_TrawlNet.FileDoesNotExistError = Ice.createTempClass()
    class FileDoesNotExistError(Ice.UserException):
        def __init__(self, info=''):
            self.info = info

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::TrawlNet::FileDoesNotExistError'

    _M_TrawlNet._t_FileDoesNotExistError = IcePy.defineException('::TrawlNet::FileDoesNotExistError', FileDoesNotExistError, (), False, None, (('info', (), IcePy._t_string, False, 0),))
    FileDoesNotExistError._ice_type = _M_TrawlNet._t_FileDoesNotExistError

    _M_TrawlNet.FileDoesNotExistError = FileDoesNotExistError
    del FileDoesNotExistError

_M_TrawlNet._t_Sender = IcePy.defineValue('::TrawlNet::Sender', Ice.Value, -1, (), False, True, None, ())

if 'SenderPrx' not in _M_TrawlNet.__dict__:
    _M_TrawlNet.SenderPrx = Ice.createTempClass()
    class SenderPrx(Ice.ObjectPrx):

        def receive(self, size, context=None):
            return _M_TrawlNet.Sender._op_receive.invoke(self, ((size, ), context))

        def receiveAsync(self, size, context=None):
            return _M_TrawlNet.Sender._op_receive.invokeAsync(self, ((size, ), context))

        def begin_receive(self, size, _response=None, _ex=None, _sent=None, context=None):
            return _M_TrawlNet.Sender._op_receive.begin(self, ((size, ), _response, _ex, _sent, context))

        def end_receive(self, _r):
            return _M_TrawlNet.Sender._op_receive.end(self, _r)

        def close(self, context=None):
            return _M_TrawlNet.Sender._op_close.invoke(self, ((), context))

        def closeAsync(self, context=None):
            return _M_TrawlNet.Sender._op_close.invokeAsync(self, ((), context))

        def begin_close(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_TrawlNet.Sender._op_close.begin(self, ((), _response, _ex, _sent, context))

        def end_close(self, _r):
            return _M_TrawlNet.Sender._op_close.end(self, _r)

        def destroy(self, context=None):
            return _M_TrawlNet.Sender._op_destroy.invoke(self, ((), context))

        def destroyAsync(self, context=None):
            return _M_TrawlNet.Sender._op_destroy.invokeAsync(self, ((), context))

        def begin_destroy(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_TrawlNet.Sender._op_destroy.begin(self, ((), _response, _ex, _sent, context))

        def end_destroy(self, _r):
            return _M_TrawlNet.Sender._op_destroy.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_TrawlNet.SenderPrx.ice_checkedCast(proxy, '::TrawlNet::Sender', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_TrawlNet.SenderPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::TrawlNet::Sender'
    _M_TrawlNet._t_SenderPrx = IcePy.defineProxy('::TrawlNet::Sender', SenderPrx)

    _M_TrawlNet.SenderPrx = SenderPrx
    del SenderPrx

    _M_TrawlNet.Sender = Ice.createTempClass()
    class Sender(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::TrawlNet::Sender')

        def ice_id(self, current=None):
            return '::TrawlNet::Sender'

        @staticmethod
        def ice_staticId():
            return '::TrawlNet::Sender'

        def receive(self, size, current=None):
            raise NotImplementedError("servant method 'receive' not implemented")

        def close(self, current=None):
            raise NotImplementedError("servant method 'close' not implemented")

        def destroy(self, current=None):
            raise NotImplementedError("servant method 'destroy' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_TrawlNet._t_SenderDisp)

        __repr__ = __str__

    _M_TrawlNet._t_SenderDisp = IcePy.defineClass('::TrawlNet::Sender', Sender, (), None, ())
    Sender._ice_type = _M_TrawlNet._t_SenderDisp

    Sender._op_receive = IcePy.Operation('receive', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), ((), IcePy._t_string, False, 0), ())
    Sender._op_close = IcePy.Operation('close', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    Sender._op_destroy = IcePy.Operation('destroy', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())

    _M_TrawlNet.Sender = Sender
    del Sender

_M_TrawlNet._t_Receiver = IcePy.defineValue('::TrawlNet::Receiver', Ice.Value, -1, (), False, True, None, ())

if 'ReceiverPrx' not in _M_TrawlNet.__dict__:
    _M_TrawlNet.ReceiverPrx = Ice.createTempClass()
    class ReceiverPrx(Ice.ObjectPrx):

        def start(self, context=None):
            return _M_TrawlNet.Receiver._op_start.invoke(self, ((), context))

        def startAsync(self, context=None):
            return _M_TrawlNet.Receiver._op_start.invokeAsync(self, ((), context))

        def begin_start(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_TrawlNet.Receiver._op_start.begin(self, ((), _response, _ex, _sent, context))

        def end_start(self, _r):
            return _M_TrawlNet.Receiver._op_start.end(self, _r)

        def destroy(self, context=None):
            return _M_TrawlNet.Receiver._op_destroy.invoke(self, ((), context))

        def destroyAsync(self, context=None):
            return _M_TrawlNet.Receiver._op_destroy.invokeAsync(self, ((), context))

        def begin_destroy(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_TrawlNet.Receiver._op_destroy.begin(self, ((), _response, _ex, _sent, context))

        def end_destroy(self, _r):
            return _M_TrawlNet.Receiver._op_destroy.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_TrawlNet.ReceiverPrx.ice_checkedCast(proxy, '::TrawlNet::Receiver', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_TrawlNet.ReceiverPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::TrawlNet::Receiver'
    _M_TrawlNet._t_ReceiverPrx = IcePy.defineProxy('::TrawlNet::Receiver', ReceiverPrx)

    _M_TrawlNet.ReceiverPrx = ReceiverPrx
    del ReceiverPrx

    _M_TrawlNet.Receiver = Ice.createTempClass()
    class Receiver(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::TrawlNet::Receiver')

        def ice_id(self, current=None):
            return '::TrawlNet::Receiver'

        @staticmethod
        def ice_staticId():
            return '::TrawlNet::Receiver'

        def start(self, current=None):
            raise NotImplementedError("servant method 'start' not implemented")

        def destroy(self, current=None):
            raise NotImplementedError("servant method 'destroy' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_TrawlNet._t_ReceiverDisp)

        __repr__ = __str__

    _M_TrawlNet._t_ReceiverDisp = IcePy.defineClass('::TrawlNet::Receiver', Receiver, (), None, ())
    Receiver._ice_type = _M_TrawlNet._t_ReceiverDisp

    Receiver._op_start = IcePy.Operation('start', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    Receiver._op_destroy = IcePy.Operation('destroy', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())

    _M_TrawlNet.Receiver = Receiver
    del Receiver

if '_t_ReceiversList' not in _M_TrawlNet.__dict__:
    _M_TrawlNet._t_ReceiversList = IcePy.defineSequence('::TrawlNet::ReceiversList', (), _M_TrawlNet._t_ReceiverPrx)

if '_t_FileList' not in _M_TrawlNet.__dict__:
    _M_TrawlNet._t_FileList = IcePy.defineSequence('::TrawlNet::FileList', (), IcePy._t_string)

_M_TrawlNet._t_Transfer = IcePy.defineValue('::TrawlNet::Transfer', Ice.Value, -1, (), False, True, None, ())

if 'TransferPrx' not in _M_TrawlNet.__dict__:
    _M_TrawlNet.TransferPrx = Ice.createTempClass()
    class TransferPrx(Ice.ObjectPrx):

        def createPeers(self, files, context=None):
            return _M_TrawlNet.Transfer._op_createPeers.invoke(self, ((files, ), context))

        def createPeersAsync(self, files, context=None):
            return _M_TrawlNet.Transfer._op_createPeers.invokeAsync(self, ((files, ), context))

        def begin_createPeers(self, files, _response=None, _ex=None, _sent=None, context=None):
            return _M_TrawlNet.Transfer._op_createPeers.begin(self, ((files, ), _response, _ex, _sent, context))

        def end_createPeers(self, _r):
            return _M_TrawlNet.Transfer._op_createPeers.end(self, _r)

        def destroyPeer(self, peerId, context=None):
            return _M_TrawlNet.Transfer._op_destroyPeer.invoke(self, ((peerId, ), context))

        def destroyPeerAsync(self, peerId, context=None):
            return _M_TrawlNet.Transfer._op_destroyPeer.invokeAsync(self, ((peerId, ), context))

        def begin_destroyPeer(self, peerId, _response=None, _ex=None, _sent=None, context=None):
            return _M_TrawlNet.Transfer._op_destroyPeer.begin(self, ((peerId, ), _response, _ex, _sent, context))

        def end_destroyPeer(self, _r):
            return _M_TrawlNet.Transfer._op_destroyPeer.end(self, _r)

        def destroy(self, context=None):
            return _M_TrawlNet.Transfer._op_destroy.invoke(self, ((), context))

        def destroyAsync(self, context=None):
            return _M_TrawlNet.Transfer._op_destroy.invokeAsync(self, ((), context))

        def begin_destroy(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_TrawlNet.Transfer._op_destroy.begin(self, ((), _response, _ex, _sent, context))

        def end_destroy(self, _r):
            return _M_TrawlNet.Transfer._op_destroy.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_TrawlNet.TransferPrx.ice_checkedCast(proxy, '::TrawlNet::Transfer', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_TrawlNet.TransferPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::TrawlNet::Transfer'
    _M_TrawlNet._t_TransferPrx = IcePy.defineProxy('::TrawlNet::Transfer', TransferPrx)

    _M_TrawlNet.TransferPrx = TransferPrx
    del TransferPrx

    _M_TrawlNet.Transfer = Ice.createTempClass()
    class Transfer(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::TrawlNet::Transfer')

        def ice_id(self, current=None):
            return '::TrawlNet::Transfer'

        @staticmethod
        def ice_staticId():
            return '::TrawlNet::Transfer'

        def createPeers(self, files, current=None):
            raise NotImplementedError("servant method 'createPeers' not implemented")

        def destroyPeer(self, peerId, current=None):
            raise NotImplementedError("servant method 'destroyPeer' not implemented")

        def destroy(self, current=None):
            raise NotImplementedError("servant method 'destroy' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_TrawlNet._t_TransferDisp)

        __repr__ = __str__

    _M_TrawlNet._t_TransferDisp = IcePy.defineClass('::TrawlNet::Transfer', Transfer, (), None, ())
    Transfer._ice_type = _M_TrawlNet._t_TransferDisp

    Transfer._op_createPeers = IcePy.Operation('createPeers', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_TrawlNet._t_FileList, False, 0),), (), ((), _M_TrawlNet._t_ReceiversList, False, 0), (_M_TrawlNet._t_FileDoesNotExistError,))
    Transfer._op_destroyPeer = IcePy.Operation('destroyPeer', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())
    Transfer._op_destroy = IcePy.Operation('destroy', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())

    _M_TrawlNet.Transfer = Transfer
    del Transfer

if 'PeerInfo' not in _M_TrawlNet.__dict__:
    _M_TrawlNet.PeerInfo = Ice.createTempClass()
    class PeerInfo(object):
        def __init__(self, transfer=None, fileName=''):
            self.transfer = transfer
            self.fileName = fileName

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_TrawlNet.PeerInfo):
                return NotImplemented
            else:
                if self.transfer != other.transfer:
                    return False
                if self.fileName != other.fileName:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_TrawlNet._t_PeerInfo)

        __repr__ = __str__

    _M_TrawlNet._t_PeerInfo = IcePy.defineStruct('::TrawlNet::PeerInfo', PeerInfo, (), (
        ('transfer', (), _M_TrawlNet._t_TransferPrx),
        ('fileName', (), IcePy._t_string)
    ))

    _M_TrawlNet.PeerInfo = PeerInfo
    del PeerInfo

_M_TrawlNet._t_SenderFactory = IcePy.defineValue('::TrawlNet::SenderFactory', Ice.Value, -1, (), False, True, None, ())

if 'SenderFactoryPrx' not in _M_TrawlNet.__dict__:
    _M_TrawlNet.SenderFactoryPrx = Ice.createTempClass()
    class SenderFactoryPrx(Ice.ObjectPrx):

        def create(self, fileName, context=None):
            return _M_TrawlNet.SenderFactory._op_create.invoke(self, ((fileName, ), context))

        def createAsync(self, fileName, context=None):
            return _M_TrawlNet.SenderFactory._op_create.invokeAsync(self, ((fileName, ), context))

        def begin_create(self, fileName, _response=None, _ex=None, _sent=None, context=None):
            return _M_TrawlNet.SenderFactory._op_create.begin(self, ((fileName, ), _response, _ex, _sent, context))

        def end_create(self, _r):
            return _M_TrawlNet.SenderFactory._op_create.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_TrawlNet.SenderFactoryPrx.ice_checkedCast(proxy, '::TrawlNet::SenderFactory', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_TrawlNet.SenderFactoryPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::TrawlNet::SenderFactory'
    _M_TrawlNet._t_SenderFactoryPrx = IcePy.defineProxy('::TrawlNet::SenderFactory', SenderFactoryPrx)

    _M_TrawlNet.SenderFactoryPrx = SenderFactoryPrx
    del SenderFactoryPrx

    _M_TrawlNet.SenderFactory = Ice.createTempClass()
    class SenderFactory(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::TrawlNet::SenderFactory')

        def ice_id(self, current=None):
            return '::TrawlNet::SenderFactory'

        @staticmethod
        def ice_staticId():
            return '::TrawlNet::SenderFactory'

        def create(self, fileName, current=None):
            raise NotImplementedError("servant method 'create' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_TrawlNet._t_SenderFactoryDisp)

        __repr__ = __str__

    _M_TrawlNet._t_SenderFactoryDisp = IcePy.defineClass('::TrawlNet::SenderFactory', SenderFactory, (), None, ())
    SenderFactory._ice_type = _M_TrawlNet._t_SenderFactoryDisp

    SenderFactory._op_create = IcePy.Operation('create', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_TrawlNet._t_SenderPrx, False, 0), (_M_TrawlNet._t_FileDoesNotExistError,))

    _M_TrawlNet.SenderFactory = SenderFactory
    del SenderFactory

_M_TrawlNet._t_ReceiverFactory = IcePy.defineValue('::TrawlNet::ReceiverFactory', Ice.Value, -1, (), False, True, None, ())

if 'ReceiverFactoryPrx' not in _M_TrawlNet.__dict__:
    _M_TrawlNet.ReceiverFactoryPrx = Ice.createTempClass()
    class ReceiverFactoryPrx(Ice.ObjectPrx):

        def create(self, fileName, sender, transfer, context=None):
            return _M_TrawlNet.ReceiverFactory._op_create.invoke(self, ((fileName, sender, transfer), context))

        def createAsync(self, fileName, sender, transfer, context=None):
            return _M_TrawlNet.ReceiverFactory._op_create.invokeAsync(self, ((fileName, sender, transfer), context))

        def begin_create(self, fileName, sender, transfer, _response=None, _ex=None, _sent=None, context=None):
            return _M_TrawlNet.ReceiverFactory._op_create.begin(self, ((fileName, sender, transfer), _response, _ex, _sent, context))

        def end_create(self, _r):
            return _M_TrawlNet.ReceiverFactory._op_create.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_TrawlNet.ReceiverFactoryPrx.ice_checkedCast(proxy, '::TrawlNet::ReceiverFactory', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_TrawlNet.ReceiverFactoryPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::TrawlNet::ReceiverFactory'
    _M_TrawlNet._t_ReceiverFactoryPrx = IcePy.defineProxy('::TrawlNet::ReceiverFactory', ReceiverFactoryPrx)

    _M_TrawlNet.ReceiverFactoryPrx = ReceiverFactoryPrx
    del ReceiverFactoryPrx

    _M_TrawlNet.ReceiverFactory = Ice.createTempClass()
    class ReceiverFactory(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::TrawlNet::ReceiverFactory')

        def ice_id(self, current=None):
            return '::TrawlNet::ReceiverFactory'

        @staticmethod
        def ice_staticId():
            return '::TrawlNet::ReceiverFactory'

        def create(self, fileName, sender, transfer, current=None):
            raise NotImplementedError("servant method 'create' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_TrawlNet._t_ReceiverFactoryDisp)

        __repr__ = __str__

    _M_TrawlNet._t_ReceiverFactoryDisp = IcePy.defineClass('::TrawlNet::ReceiverFactory', ReceiverFactory, (), None, ())
    ReceiverFactory._ice_type = _M_TrawlNet._t_ReceiverFactoryDisp

    ReceiverFactory._op_create = IcePy.Operation('create', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), _M_TrawlNet._t_SenderPrx, False, 0), ((), _M_TrawlNet._t_TransferPrx, False, 0)), (), ((), _M_TrawlNet._t_ReceiverPrx, False, 0), ())

    _M_TrawlNet.ReceiverFactory = ReceiverFactory
    del ReceiverFactory

_M_TrawlNet._t_TransferFactory = IcePy.defineValue('::TrawlNet::TransferFactory', Ice.Value, -1, (), False, True, None, ())

if 'TransferFactoryPrx' not in _M_TrawlNet.__dict__:
    _M_TrawlNet.TransferFactoryPrx = Ice.createTempClass()
    class TransferFactoryPrx(Ice.ObjectPrx):

        def newTransfer(self, receiverFactory, context=None):
            return _M_TrawlNet.TransferFactory._op_newTransfer.invoke(self, ((receiverFactory, ), context))

        def newTransferAsync(self, receiverFactory, context=None):
            return _M_TrawlNet.TransferFactory._op_newTransfer.invokeAsync(self, ((receiverFactory, ), context))

        def begin_newTransfer(self, receiverFactory, _response=None, _ex=None, _sent=None, context=None):
            return _M_TrawlNet.TransferFactory._op_newTransfer.begin(self, ((receiverFactory, ), _response, _ex, _sent, context))

        def end_newTransfer(self, _r):
            return _M_TrawlNet.TransferFactory._op_newTransfer.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_TrawlNet.TransferFactoryPrx.ice_checkedCast(proxy, '::TrawlNet::TransferFactory', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_TrawlNet.TransferFactoryPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::TrawlNet::TransferFactory'
    _M_TrawlNet._t_TransferFactoryPrx = IcePy.defineProxy('::TrawlNet::TransferFactory', TransferFactoryPrx)

    _M_TrawlNet.TransferFactoryPrx = TransferFactoryPrx
    del TransferFactoryPrx

    _M_TrawlNet.TransferFactory = Ice.createTempClass()
    class TransferFactory(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::TrawlNet::TransferFactory')

        def ice_id(self, current=None):
            return '::TrawlNet::TransferFactory'

        @staticmethod
        def ice_staticId():
            return '::TrawlNet::TransferFactory'

        def newTransfer(self, receiverFactory, current=None):
            raise NotImplementedError("servant method 'newTransfer' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_TrawlNet._t_TransferFactoryDisp)

        __repr__ = __str__

    _M_TrawlNet._t_TransferFactoryDisp = IcePy.defineClass('::TrawlNet::TransferFactory', TransferFactory, (), None, ())
    TransferFactory._ice_type = _M_TrawlNet._t_TransferFactoryDisp

    TransferFactory._op_newTransfer = IcePy.Operation('newTransfer', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_TrawlNet._t_ReceiverFactoryPrx, False, 0),), (), ((), _M_TrawlNet._t_TransferPrx, False, 0), ())

    _M_TrawlNet.TransferFactory = TransferFactory
    del TransferFactory

_M_TrawlNet._t_PeerEvent = IcePy.defineValue('::TrawlNet::PeerEvent', Ice.Value, -1, (), False, True, None, ())

if 'PeerEventPrx' not in _M_TrawlNet.__dict__:
    _M_TrawlNet.PeerEventPrx = Ice.createTempClass()
    class PeerEventPrx(Ice.ObjectPrx):

        def peerFinished(self, peerInfo, context=None):
            return _M_TrawlNet.PeerEvent._op_peerFinished.invoke(self, ((peerInfo, ), context))

        def peerFinishedAsync(self, peerInfo, context=None):
            return _M_TrawlNet.PeerEvent._op_peerFinished.invokeAsync(self, ((peerInfo, ), context))

        def begin_peerFinished(self, peerInfo, _response=None, _ex=None, _sent=None, context=None):
            return _M_TrawlNet.PeerEvent._op_peerFinished.begin(self, ((peerInfo, ), _response, _ex, _sent, context))

        def end_peerFinished(self, _r):
            return _M_TrawlNet.PeerEvent._op_peerFinished.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_TrawlNet.PeerEventPrx.ice_checkedCast(proxy, '::TrawlNet::PeerEvent', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_TrawlNet.PeerEventPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::TrawlNet::PeerEvent'
    _M_TrawlNet._t_PeerEventPrx = IcePy.defineProxy('::TrawlNet::PeerEvent', PeerEventPrx)

    _M_TrawlNet.PeerEventPrx = PeerEventPrx
    del PeerEventPrx

    _M_TrawlNet.PeerEvent = Ice.createTempClass()
    class PeerEvent(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::TrawlNet::PeerEvent')

        def ice_id(self, current=None):
            return '::TrawlNet::PeerEvent'

        @staticmethod
        def ice_staticId():
            return '::TrawlNet::PeerEvent'

        def peerFinished(self, peerInfo, current=None):
            raise NotImplementedError("servant method 'peerFinished' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_TrawlNet._t_PeerEventDisp)

        __repr__ = __str__

    _M_TrawlNet._t_PeerEventDisp = IcePy.defineClass('::TrawlNet::PeerEvent', PeerEvent, (), None, ())
    PeerEvent._ice_type = _M_TrawlNet._t_PeerEventDisp

    PeerEvent._op_peerFinished = IcePy.Operation('peerFinished', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_TrawlNet._t_PeerInfo, False, 0),), (), None, ())

    _M_TrawlNet.PeerEvent = PeerEvent
    del PeerEvent

_M_TrawlNet._t_TransferEvent = IcePy.defineValue('::TrawlNet::TransferEvent', Ice.Value, -1, (), False, True, None, ())

if 'TransferEventPrx' not in _M_TrawlNet.__dict__:
    _M_TrawlNet.TransferEventPrx = Ice.createTempClass()
    class TransferEventPrx(Ice.ObjectPrx):

        def transferFinished(self, transfer, context=None):
            return _M_TrawlNet.TransferEvent._op_transferFinished.invoke(self, ((transfer, ), context))

        def transferFinishedAsync(self, transfer, context=None):
            return _M_TrawlNet.TransferEvent._op_transferFinished.invokeAsync(self, ((transfer, ), context))

        def begin_transferFinished(self, transfer, _response=None, _ex=None, _sent=None, context=None):
            return _M_TrawlNet.TransferEvent._op_transferFinished.begin(self, ((transfer, ), _response, _ex, _sent, context))

        def end_transferFinished(self, _r):
            return _M_TrawlNet.TransferEvent._op_transferFinished.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_TrawlNet.TransferEventPrx.ice_checkedCast(proxy, '::TrawlNet::TransferEvent', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_TrawlNet.TransferEventPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::TrawlNet::TransferEvent'
    _M_TrawlNet._t_TransferEventPrx = IcePy.defineProxy('::TrawlNet::TransferEvent', TransferEventPrx)

    _M_TrawlNet.TransferEventPrx = TransferEventPrx
    del TransferEventPrx

    _M_TrawlNet.TransferEvent = Ice.createTempClass()
    class TransferEvent(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::TrawlNet::TransferEvent')

        def ice_id(self, current=None):
            return '::TrawlNet::TransferEvent'

        @staticmethod
        def ice_staticId():
            return '::TrawlNet::TransferEvent'

        def transferFinished(self, transfer, current=None):
            raise NotImplementedError("servant method 'transferFinished' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_TrawlNet._t_TransferEventDisp)

        __repr__ = __str__

    _M_TrawlNet._t_TransferEventDisp = IcePy.defineClass('::TrawlNet::TransferEvent', TransferEvent, (), None, ())
    TransferEvent._ice_type = _M_TrawlNet._t_TransferEventDisp

    TransferEvent._op_transferFinished = IcePy.Operation('transferFinished', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_TrawlNet._t_TransferPrx, False, 0),), (), None, ())

    _M_TrawlNet.TransferEvent = TransferEvent
    del TransferEvent

# End of module TrawlNet
