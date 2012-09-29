# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import os
from pyrrd.rrd import DataSource, RRA, RRD
import simplejson

rrdPath = 'public/rrds/'

def list(req):
	rrds = os.listdir(rrdPath)
	return render_to_response('rrd/list.html', {'rrds': rrds})

def info(req, rrd):
	if os.path.isfile(rrdPath+rrd):
		filename = rrd
		rrd = RRD(rrdPath+rrd, mode='r')
		info = rrd.getData()
		info['filename'] = filename
		return render_to_response('rrd/info.html', {'info': info})

def raw(req, rrd):
        if os.path.isfile(rrdPath+rrd):
		filename = rrd
                rrd = RRD(rrdPath+rrd, mode='r')
                info = rrd.getData()
		info['filename'] = filename
        	return render_to_response('rrd/raw.html', {'info': info})

def graph(req, rrd):
        if os.path.isfile(rrdPath+rrd):
                filename = rrd
                rrd = RRD(rrdPath+rrd, mode='r')
                info = rrd.getData()
                info['filename'] = filename
                return render_to_response('rrd/graph.html', {'info': info})

def data(req, rrd, ds, rra):
        if os.path.isfile(rrdPath+rrd):
                rrd = RRD(rrdPath+rrd, mode='r')
		info = rrd.getData()
		step = info[rra]['step']
		start = info['lastupdate'] - info[rra]['rows']*step
                data = rrd.fetch(resolution=step, start=start, end=info['lastupdate'])
        	return HttpResponse(simplejson.dumps(data))
