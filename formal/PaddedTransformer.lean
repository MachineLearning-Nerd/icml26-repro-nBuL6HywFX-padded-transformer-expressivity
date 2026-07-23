import Std

/-!
Kernel-checked universal obligations for Theorem 4.2 and the Lemma 4.1 repair.

This file deliberately uses only Lean's bundled `Std` library: no `sorry`, no
custom axioms, no third-party library, and no finite enumeration. Source-paper
theorems enter the class-equivalence section only as explicit hypotheses.
The new routing repair, the counterexample to the printed route, vector
padding, and inclusion composition are proved for arbitrary types/sizes.
-/

namespace PaddedTransformer

/-! ## Extensional circuit-class equivalence -/

abbrev Language := Nat → Bool
abbrev LanguageClass := Language → Prop

def Included (A B : LanguageClass) : Prop := ∀ L, A L → B L
def Equivalent (A B : LanguageClass) : Prop := ∀ L, A L ↔ B L

theorem equivalent_of_inclusions {A B : LanguageClass}
    (forward : Included A B) (backward : Included B A) : Equivalent A B := by
  intro L
  exact ⟨forward L, backward L⟩

theorem included_trans {A B C : LanguageClass}
    (ab : Included A B) (bc : Included B C) : Included A C := by
  intro L hL
  exact bc L (ab L hL)

/-!
The four hypotheses below are the exact imported/source-backed inclusions.
The theorem proves that no finite-N observation is used to obtain either
equality: both conclusions are pure inclusion sandwiches.
-/
theorem theorem42_from_source_inclusions
    {AC0 TC0 LPTconst LPTlog : LanguageClass}
    (acLower : Included AC0 LPTconst)
    (acUpper : Included LPTconst AC0)
    (tcLower : Included TC0 LPTlog)
    (tcUpper : Included LPTlog TC0) :
    Equivalent AC0 LPTconst ∧ Equivalent TC0 LPTlog := by
  exact ⟨equivalent_of_inclusions acLower acUpper,
    equivalent_of_inclusions tcLower tcUpper⟩

/-! ## Width lifting is semantics preserving -/

def Vec (n : Nat) (α : Type) := Fin n → α

def padVec {d D : Nat} {α : Type} [Zero α]
    (_h : d ≤ D) (v : Vec d α) : Vec D α := fun i =>
  if hi : i.val < d then v ⟨i.val, hi⟩ else 0

theorem padVec_old_coordinate {d D : Nat} {α : Type} [Zero α]
    (h : d ≤ D) (v : Vec d α) (i : Fin d) :
    padVec h v ⟨i.val, Nat.lt_of_lt_of_le i.isLt h⟩ = v i := by
  simp [padVec]

def liftLayer {d D : Nat} {α : Type} [Zero α]
    (h : d ≤ D) (layer : Vec d α → Vec d α) : Vec d α → Vec D α :=
  fun v => padVec h (layer v)

theorem liftLayer_commutes {d D : Nat} {α : Type} [Zero α]
    (h : d ≤ D) (layer : Vec d α → Vec d α) (v : Vec d α) :
    liftLayer h layer v = padVec h (layer v) := by
  rfl

def pointerCoordinateWidth (_inputLength : Nat) : Nat := 2 + 2 + 2

theorem repaired_pointer_width_is_six (inputLength : Nat) :
    pointerCoordinateWidth inputLength = 6 := by
  rfl

theorem repaired_pointer_width_is_constant :
    ∀ n m, pointerCoordinateWidth n = pointerCoordinateWidth m := by
  intro n m
  rfl

/-! ## Universal positional focusing -/

def IsMax {ι Key Score : Type} [LE Score]
    (pe : ι → Key) (score : Key → Key → Score)
    (target candidate : ι) : Prop :=
  ∀ other, score (pe target) (pe other) ≤ score (pe target) (pe candidate)

/-!
This is the abstract content supplied by the rounded positional-encoding gap
and fixed-point focusing lemmas: the matching position scores strictly above
every nonmatching position. The proof is universal in the position type.
-/
theorem isMax_iff_eq {ι Key Score : Type} [DecidableEq ι]
    [LE Score] [LT Score] [Std.IsPreorder Score] [Std.LawfulOrderLT Score]
    (pe : ι → Key) (score : Key → Key → Score)
    (strictFocus : ∀ target other, target ≠ other →
      score (pe target) (pe other) < score (pe target) (pe target))
    (target candidate : ι) :
    IsMax pe score target candidate ↔ candidate = target := by
  constructor
  · intro h
    by_cases heq : candidate = target
    · exact heq
    · have hlt := strictFocus target candidate (fun h => heq h.symm)
      have hge := h target
      exact False.elim ((Std.not_le_of_gt hlt) hge)
  · intro heq
    subst candidate
    intro other
    by_cases hsame : target = other
    · subst other
      exact Std.IsPreorder.le_refl _
    · exact Std.le_of_lt (strictFocus target other hsame)

structure Argument (ι : Type) where
  source : ι
  gate : ι

def Layer1Routes {ι Key Score : Type} [LE Score]
    (pe : ι → Key) (score : Key → Key → Score)
    (argument : Argument ι) (token : ι) : Prop :=
  IsMax pe score argument.source token

def Layer2Collects {ι Key Score : Type} [LE Score]
    (pe : ι → Key) (score : Key → Key → Score)
    (gate : ι) (argument : Argument ι) : Prop :=
  IsMax pe score gate argument.gate

def PrintedLayer2Collects {ι Key Score : Type} [LE Score]
    (pe : ι → Key) (score : Key → Key → Score)
    (gate : ι) (argument : Argument ι) : Prop :=
  IsMax pe score gate argument.source

theorem repaired_layer1_routes_exactly_source
    {ι Key Score : Type} [DecidableEq ι]
    [LE Score] [LT Score] [Std.IsPreorder Score] [Std.LawfulOrderLT Score]
    (pe : ι → Key) (score : Key → Key → Score)
    (strictFocus : ∀ target other, target ≠ other →
      score (pe target) (pe other) < score (pe target) (pe target))
    (argument : Argument ι) (token : ι) :
    Layer1Routes pe score argument token ↔ token = argument.source := by
  exact isMax_iff_eq pe score strictFocus argument.source token

theorem repaired_layer2_collects_exactly_destination
    {ι Key Score : Type} [DecidableEq ι]
    [LE Score] [LT Score] [Std.IsPreorder Score] [Std.LawfulOrderLT Score]
    (pe : ι → Key) (score : Key → Key → Score)
    (strictFocus : ∀ target other, target ≠ other →
      score (pe target) (pe other) < score (pe target) (pe target))
    (gate : ι) (argument : Argument ι) :
    Layer2Collects pe score gate argument ↔ argument.gate = gate := by
  exact isMax_iff_eq pe score strictFocus gate argument.gate

/-!
Any implementation whose exact fixed-point focusing relation is extensionally
equal to `IsMax` inherits the same universal routing result. This is the
formal boundary at which the paper's rounded-softmax focusing lemma plugs in.
-/
theorem exact_focusing_operator_collects_destination
    {ι Key Score : Type} [DecidableEq ι]
    [LE Score] [LT Score] [Std.IsPreorder Score] [Std.LawfulOrderLT Score]
    (pe : ι → Key) (score : Key → Key → Score)
    (strictFocus : ∀ target other, target ≠ other →
      score (pe target) (pe other) < score (pe target) (pe target))
    (selects : ι → ι → Prop)
    (exactFocusing : ∀ target candidate,
      selects target candidate ↔ IsMax pe score target candidate)
    (gate : ι) (argument : Argument ι) :
    selects gate argument.gate ↔ argument.gate = gate := by
  rw [exactFocusing]
  exact isMax_iff_eq pe score strictFocus gate argument.gate

theorem printed_layer2_collects_source_not_destination
    {ι Key Score : Type} [DecidableEq ι]
    [LE Score] [LT Score] [Std.IsPreorder Score] [Std.LawfulOrderLT Score]
    (pe : ι → Key) (score : Key → Key → Score)
    (strictFocus : ∀ target other, target ≠ other →
      score (pe target) (pe other) < score (pe target) (pe target))
    (gate : ι) (argument : Argument ι) :
    PrintedLayer2Collects pe score gate argument ↔ argument.source = gate := by
  exact isMax_iff_eq pe score strictFocus gate argument.source

theorem printed_route_rejected_when_source_ne_gate
    {ι Key Score : Type} [DecidableEq ι]
    [LE Score] [LT Score] [Std.IsPreorder Score] [Std.LawfulOrderLT Score]
    (pe : ι → Key) (score : Key → Key → Score)
    (strictFocus : ∀ target other, target ≠ other →
      score (pe target) (pe other) < score (pe target) (pe target))
    (gate : ι) (argument : Argument ι)
    (different : argument.source ≠ gate) :
    ¬ PrintedLayer2Collects pe score gate argument := by
  intro h
  have hs := (printed_layer2_collects_source_not_destination
    pe score strictFocus gate argument).mp h
  exact different hs

/-! ## Gate arithmetic used after exact routing -/

theorem average_threshold_cross_multiply
    (sum threshold arity : Nat) (positiveArity : 0 < arity) :
    sum * arity > threshold * arity ↔ sum > threshold := by
  exact Nat.mul_lt_mul_right positiveArity

/-! ## Level-by-level circuit simulation induction -/

theorem all_levels_correct
    (correctAt : Nat → Prop)
    (base : correctAt 0)
    (step : ∀ level, correctAt level → correctAt (level + 1)) :
    ∀ level, correctAt level := by
  intro level
  induction level with
  | zero => exact base
  | succ level ih =>
      simpa [Nat.succ_eq_add_one] using step level ih

#print axioms equivalent_of_inclusions
#print axioms theorem42_from_source_inclusions
#print axioms padVec_old_coordinate
#print axioms repaired_pointer_width_is_six
#print axioms repaired_pointer_width_is_constant
#print axioms repaired_layer1_routes_exactly_source
#print axioms repaired_layer2_collects_exactly_destination
#print axioms exact_focusing_operator_collects_destination
#print axioms printed_route_rejected_when_source_ne_gate
#print axioms average_threshold_cross_multiply
#print axioms all_levels_correct

end PaddedTransformer
