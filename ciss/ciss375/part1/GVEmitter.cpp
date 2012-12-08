#include <iostream>

#include "AST.h"
#include "GVEmitter.h"

using std::cout;
using std::endl;

// You MUST fill in implementation for each of these functions, plus
// any additional function that you define in GVEmitter.h
//
// You will probably do a lot of cut-and-paste; many node types behave
// very similarly.  Think about adding additional functions to cut down
// on the repetition.

GVEmitter::GVEmitter()
{

}

void GVEmitter::visit(Number * n)
{
}


void GVEmitter::visit(Plus * n)
{
}


void GVEmitter::visit(Minus * n)
{
}


void GVEmitter::visit(Times * n)
{
}


void GVEmitter::visit(Divide * n)
{
}


void GVEmitter::visit(Id * id)
{
}


void GVEmitter::visit(LessThan * n)
{
}

void GVEmitter::visit(GreaterThan * n)
{
}

void GVEmitter::visit(EqualTo * n)
{
}

void GVEmitter::visit(If * ifNode)
{
}

void GVEmitter::visit(While * n)
{
}

void GVEmitter::visit(Block * n)
{
}

void GVEmitter::visit(SList * n)
{
}

void GVEmitter::visit(Assign * a)
{
}

void GVEmitter::visit(Declaration * a)
{
}

void GVEmitter::visit(Read * r)
{
}

void GVEmitter::visit(Write * w)
{
}

void GVEmitter::visit(Pass * w)
{
}
