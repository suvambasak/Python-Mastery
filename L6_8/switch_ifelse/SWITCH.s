	.file	"assembly.c"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	$1000, -4(%rbp)
	cmpl	$10, -4(%rbp)
	ja	.L2
	movl	-4(%rbp), %eax
	leaq	0(,%rax,4), %rdx
	leaq	.L4(%rip), %rax
	movl	(%rdx,%rax), %eax
	cltq
	leaq	.L4(%rip), %rdx
	addq	%rdx, %rax
	notrack jmp	*%rax
	.section	.rodata
	.align 4
	.align 4
.L4:
	.long	.L14-.L4
	.long	.L13-.L4
	.long	.L12-.L4
	.long	.L11-.L4
	.long	.L10-.L4
	.long	.L9-.L4
	.long	.L8-.L4
	.long	.L7-.L4
	.long	.L6-.L4
	.long	.L5-.L4
	.long	.L3-.L4
	.text
.L3:
	movl	$65, %eax
	jmp	.L15
.L5:
	movl	$66, %eax
	jmp	.L15
.L6:
	movl	$67, %eax
	jmp	.L15
.L7:
	movl	$68, %eax
	jmp	.L15
.L8:
	movl	$69, %eax
	jmp	.L15
.L9:
	movl	$70, %eax
	jmp	.L15
.L10:
	movl	$71, %eax
	jmp	.L15
.L11:
	movl	$71, %eax
	jmp	.L15
.L12:
	movl	$73, %eax
	jmp	.L15
.L13:
	movl	$74, %eax
	jmp	.L15
.L14:
	movl	$75, %eax
	jmp	.L15
.L2:
	movl	$69, %eax
.L15:
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 9.5.0-1ubuntu1~22.04) 9.5.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
