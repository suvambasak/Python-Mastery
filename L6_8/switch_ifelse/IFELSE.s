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
	jne	.L2
	movl	$65, %eax
	jmp	.L3
.L2:
	cmpl	$9, -4(%rbp)
	jne	.L4
	movl	$66, %eax
	jmp	.L3
.L4:
	cmpl	$8, -4(%rbp)
	jne	.L5
	movl	$67, %eax
	jmp	.L3
.L5:
	cmpl	$7, -4(%rbp)
	jne	.L6
	movl	$68, %eax
	jmp	.L3
.L6:
	cmpl	$6, -4(%rbp)
	jne	.L7
	movl	$69, %eax
	jmp	.L3
.L7:
	cmpl	$5, -4(%rbp)
	jne	.L8
	movl	$70, %eax
	jmp	.L3
.L8:
	cmpl	$4, -4(%rbp)
	jne	.L9
	movl	$71, %eax
	jmp	.L3
.L9:
	cmpl	$3, -4(%rbp)
	jne	.L10
	movl	$71, %eax
	jmp	.L3
.L10:
	cmpl	$2, -4(%rbp)
	jne	.L11
	movl	$73, %eax
	jmp	.L3
.L11:
	cmpl	$1, -4(%rbp)
	jne	.L12
	movl	$74, %eax
	jmp	.L3
.L12:
	cmpl	$0, -4(%rbp)
	jne	.L13
	movl	$75, %eax
	jmp	.L3
.L13:
	movl	$69, %eax
.L3:
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
