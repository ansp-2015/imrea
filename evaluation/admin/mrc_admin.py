# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _, ugettext
from django.contrib.admin.utils import (unquote,)
from reversion_compare.helpers import patch_admin
import logging
from .base_admin import BaseAdmin
from evaluation.models.mrc import MRC
from ..forms import MRCForm


class MRCAdmin(BaseAdmin):
    """
    Visual Analog Scale
    """

    TEXT_SHOULDER_ABDUCTION = _(u"""
<div class="main-test">
<strong>For Normal</strong>: maintains the end position of the test against a maximum downward resistance.<br />
<strong>Good</strong>: Holds the end position of the test against a strong to moderate resistance down.<br />
<strong>Regular</strong>: complete the range of movement up to 90° without any manual resistance.<br />
</div>
<strong>Preliminary assessment</strong>:<br />
The examiner should check the full range of shoulder motion on all planes and observe the scapula for stability and
regularity of movement. Consult the test for scapular abduction and upward rotation.

<div class="panel-body"><strong>Scapular abduction and upward rotation</strong><br />
<strong>Patient position</strong>: Sitting with the forward arm flexed to approximately 130° and then stretched in this
plane as far as it can move.<br />
<strong>Therapist's position</strong>: Standing on the side of the patient to be tested. The hand used to apply
resistance in a downward and backward direction. The other hand stabilizes the trunk immediately below the scapula on
the same side; this prevents rotation of the trunk. The examiner should choose a location on the wall or ceiling that
can act as a target to be reached by the patient in a line with approximately 130 degrees of flexion.<br />
<strong>Test</strong>: The patient performs abduction and rotation up the scapula by stretching and raising the arm to
approximately 130° flexion. The patient then holds this position against maximum resistance.<br />
<strong>Patient instructions</strong>: "Raise your arm and try to reach the target on the wall."
</div>

<strong>Patient position</strong>:<br />
Sitting with the arm to the side and elbow in slight flexion.<br />
<strong>Therapist position:</strong>:<br />
Standing behind the patient. The hand that applies resistance is placed on the arm just above the elbow.<br />
<strong>Test</strong>:<br />
The patient performs abduction of the arm up to 90°.<br />
<strong>Instructions to the patient</strong>:<br />
Lift your arm away from the side of the body to shoulder level. Hold this position. Do not let me push you down.<br />
<br />

<div class="main-test">
<strong>For Precarious</strong>: completes a partial range of motion
</div>

<strong>Patient Position</strong>:<br />
Sitting with the arm to the side and slight flexion of the elbow.<br />
<strong>Therapist position</strong>:<br />
Standing behind the patient to palpate the muscles on the side being tested. Palpate the deltoid laterally to the
acromion in the upper part of the shoulder. The supraspinatus can be palpated by placing the fingers deep under the
trapezius in the supraspinous fossa of the scapula.<br />

<strong>Test</strong>:<br />
The patient tries to perform abduction of the arm.<br />
<strong>Instructions to the patient</strong>:<br />
"Try to raise the arm away from the side of the body."<br />
<br />
<div class="alternative-test">
<strong>Alternative test</strong>
</div>
<strong>Patient Position</strong>:<br />
Supine. The arm is abducted up to 90°, but is supported on the table with the elbow in slight flexion.<br />
<strong>Therapist position</strong>:<br />
Standing on the side of the patient being tested. The hand used to perform the palpation is positioned as described
for the precarious test.<br />
<strong>Test</strong>:<br />
The patient tries to perform the abduction of the shoulder by sliding the arm on the table without turning it.<br />
<strong>Instructions to the patient</strong>:<br />
"Take your arm away from the side of the body."<br />
<br />
<div class="main-test">
<strong>For Trace</strong> palpable or visible contraction of the deltoid without any movement<br />
<strong>Zero</strong>: no contractile activity
</div>

<strong>Patient Position</strong>:<br />
Seated<br />
<strong>Therapist position</strong>:<br />
Standing behind and beside the patient. The therapist holds the arm to be tested with the shoulder at approximately 
90° of abduction providing limb support at the level of the elbow<br />
<strong>Test</strong>:<br />
The patient tries to keep the arm in abduction<br />
<strong>Instructions to the patient</strong>:<br />
"Try to keep your arm in that position."<br />
<br />

<div class="alternative-test">
<strong>Alternative test</strong>
</div>

<strong>Patient Position</strong>:<br />
Dorsal decubitus with arm at side and elbow in slight flexion.<br />
<strong>Therapist position</strong>:<br />
Stand by the table in a place where the deltoid can be reached. Palpate the deltoid on the lateral surface of the upper
third of the arm.<br />
    """)

    TEXT_SHOULDER_ABDUCTION_AFTER = _(u"""
<strong>REPLACEMENT BY BRAQUIAL BICEPS</strong><br />
When the patient uses the biceps to replace, the shoulder will rotate externally and the elbow will flex. The arm will
be raised, but not by the action of the abductor muscles. To avoid this replacement, start the arm test in a few
degrees of elbow flexion, but do not allow the active contraction of the biceps during the test.<br />
<br />
<strong>USEFUL SUGGESTIONS</strong><br />
<ol>
<li>By turning the face to the opposite side and extending the pectus, the trapezius becomes looser and becomes the
most accessible supraspinatus for palpation.</li>
<li>The deltoid and supraspinatus work in sequence and when one of them is active in abduction, the other will also be
active. Palpation is only necessary when suspicion of supraspinatus weakness is suspected.</li>
<li>Do not allow shoulder elevation or lateral flexion of the trunk to the opposite side, as these movements can create
an illusion of abduction.</li>
</ol>
    """)

    TEXT_SHOULDER_FLEXION = _(u"""
<div class="main-test">
<strong>For Grade 5<br />
Grade 4<br />
Grade 3</strong>
</div>

<strong>Patient position</strong>:<br />
The patient is seated with the shoulder at 0 ° of flexion, the arm at the side of the body, the elbow extended and the
palm facing the trunk.<br />

<strong>Stabilization / Palpation</strong>:<br />
The examiner performs stabilization on the upper ipsilateral shoulder, taking care to avoid pressure on the anterior
deltoid fibers. The other hand palpates the anterior deltoid fibers for a contraction during patient movement.<br />

<strong>Examiner's action</strong>:<br />
Tell the patient, "When I ask you, I want you to move your arm just like that." As you verbalize this command, move the
patient's arm to 90 ° of shoulder flexion. By conducting the patient passively through movement, you can determine your
available ROM and let him know what the exact movement you want.<br />

<strong>Instructions to the patient</strong>:<br />
"Lift your arm now as I showed you and hold it in this position. Keep your arm in this position and do not let me move
it."<br />

<strong>Resistance</strong>:<br />
The resistance is applied immediately above the elbow in the direction of the shoulder extension. The palpating hand is
moved to the distal humerus to apply the resistance.<br />
<br />

<div class="main-test">
<strong>For Grade 2<br />
Grade 1<br />
Grade 0</strong>
</div>

<strong>Patient position</strong>:<br />
The patient lies in the lateral position with the arm to be tested upwards and supported on a dusted board. Powder and
a cloth can be placed between the limb and the bearing surface to reduce friction. The patient initiates the movement
positioned at 0° of shoulder flexion, with the palm facing the trunk.<br />

<strong>Stabilization / Palpation</strong>:<br />
The examiner performs stabilization on the upper part of the ipsilateral shoulder, taking care to avoid pressure on the
anterior deltoid fibers. The other hand palpates the fibers of the deltoid for possible contraction during patient
movement.<br />

<strong>Examiner's action</strong>:<br />
Tell the patient, "When I ask you, I want you to move your arm just like that." As you verbalize this command, move the
patient's arm to 90° of shoulder flexion. By conducting the patient passively through movement, you can determine your
available ROM and let him know what the exact movement you want.<br />

<strong>Instructions to the patient</strong>:<br />
"Now move your arm as I showed you."<br />
<br />

<strong>COMMON REPLACEMENT</strong><br />
Brachial biceps - long portion: The patient will rotate the humerus laterally during shoulder flexion. This can be
controlled by maintaining a neutral position of the humerus during the test.<br />
<br />
<div class="alternative-test">
<strong>Shoulder flexion - alternative test</strong>
</div>
<br />
<div class="main-test">
<strong>For Grade 5<br />
Grade 4</strong>
</div>

This test is intended to minimize the activity of the biceps brachii (which is achieved by flexing the elbow) and the
pectoralis major (which is achieved by keeping the shoulder in partial abduction) during flexion of the shoulder. Thus,
the relative activity of the anterior deltoid is theoretically higher at this test position, which is similar to the
test recommended by Kendall et. Al. (1993)<br />

<strong>Patient position</strong>:<br />
The patient is seated with the arm at the side of the body, the elbow at 90 ° flexion, keeping the shoulder in
slight lateral rotation.<br />

<strong>Stabilization / Palpation</strong>:<br />
The examiner performs stabilization on the upper ipsilateral shoulder, taking care to avoid pressure on the anterior
deltoid fibers. The anterior deltoid fibers are palpated immediately below the anterior part of the acromion with the
hand that is not performing stabilization.<br />

<strong>Examiner's action</strong>:<br />
Tell the patient, "When I ask you, I want you to move your arm just like that." As you verbalize this command, move the
patient's arm 90 ° in a plane midway between flexion and abduction. The elbow should remain in flexion and the shoulder
in slight lateral rotation. Once the movement is demonstrated, return the patient to the initial position. By
conducting the patient passively through movement, you can determine your available ROM and let him know what the exact
movement you want.<br />

<strong>Instructions to the patient</strong>:<br />
"Now raise your arm as I showed you and hold it in this position. Keep your arm in this position and do not let me
move you."<br />

<strong>Resistance</strong>:<br />
The resistance is applied immediately above the elbow, in the direction of extension and adduction. The palpating hand
is moved to the distal humerus to apply the resistance.<br />

<div class="main-test">
<strong>For Grade 3<br />
Grade 2<br />
Grade 1<br />
Grade 0</strong>
</div>

There is no separate test of this muscle for the grades below 3. The graduation is thus altered to accommodate the
absence of a position with the eliminated severity.<br />

For Grade 3: The patient moves the joint through full ROM without resistance.<br />
For Grade 2: The patient moves the joint through the partial ROM.<br />
For grade 1: There is no movement, but there is a palpable contraction. Palpation is done as described above
(alternative test).<br />
For degree 0: There is no movement or contraction.<br />
    """)

    TEXT_SHOULDER_LATERAL_ROTATION = _(u"""
<div class="main-test">
<strong>For Grade 5<br />
Grade 4<br />
Grade 3</strong>
</div>

<strong>Patient position</strong>:<br />
The patient is in a prone position with the shoulder at 90 ° of abduction, the elbow flexed at 90° and the forearm
hanging vertically at the side of the table. A folded towel should be placed between the patient's humerus and the
table to keep the humerus horizontal.<br />

<strong>Stabilization / Palpation</strong>:<br />
The examiner performs stabilization on the ipisilateral hemithorax (or on the scapula if the scapular stabilizers are
weak, however, care must be taken to avoid any pressure on the muscles tested). The other hand is used to palpate a
possible contraction of the infra-spinal and small round muscles. The muscles can be palpated below the spine of the
scapula, on the posterior surface of the body (infra-spinal) and axillary border (small round) of the scapula.<br />

<strong>Examiner's action</strong>:<br />
Tell the patient, "When I ask you, I want you to move your arm just like that." As you verbalize this command, rotate
the patient's side laterally, keeping the elbow in the flexed position. Once the movement is demonstrated, return the
patient to the initial position. By conducting the patient passively through movement, you can determine your available
ROM and let him know what the exact movement you want.<br />

<strong>Instructions to the patient</strong>:<br />
"Now move your arm as I showed you and hold it in this position. Keep your arm in this position and do not let me move
it."<br />

<strong>Resistance</strong>:<br />
The resistance is applied immediately above the wrist in the direction of the medial rotation of the shoulder. The
palpating hand is transferred to the distal humerus to apply the resistance.<br />
<br />

<div class="main-test">
<strong>For Grade 2<br />
Grade 1<br />
Grade 0</strong>
</div>

<strong>Patient position</strong>:<br />
The patient lies in the ventral decubitus with the shoulder at 90° of flexion and in full medial rotation, the elbow
extended and the arm hanging vertically at the side of the table.<br />

<strong>Stabilization / Palpation</strong>:<br />
The examiner performs stabilization on the ipsilateral hemithorax (or on the scapula if the stabilizers are weak,
however, care should be taken to avoid any pressure on the muscles tested). The other hand is used to palpate a
possible muscle contraction of the infra-spinal and small round (see test with gravity as resistance).<br />

<strong>Examiner's action</strong>:<br />
Tell the patient, "When I ask you, I want you to move your arm just like that." As you verbalize this command, rotate
the patient's side laterally, keeping the elbow extended. Once the movement is demonstrated, return the patient to the
initial position. By conducting the patient passively through movement, you can determine your available ROM and let
him know what the exact movement you want.<br />

<strong>Instructions to the patient</strong>:<br />
"Now move your arm as I showed you."<br />
    """)

    TEXT_SHOULDER_LATERAL_ROTATION_AFTER = _(u"""
<strong>COMMON REPLACEMENT</strong><br />
During the test with severity removed, it may appear that the patient is rotating the humerus laterally through forearm
supination. Care should be taken to make sure that movement is occurring in the glenohumeral joint.<br />
    """)

    TEXT_ELBOW_FLEXION = _(u"""
<div class="main-test">
<strong>To Normal</strong>: completes the available range and holds it firmly against a maximum resistance.<br />
<strong>Good</strong>: Complete the available range against a strong to moderate resistance, but the endpoint can not
be firm.<br />
<strong>Regular</strong>: Complete the available range with each position of the forearm without any manual resistance.
<br />
</div>

<strong>Patient Position</strong>:<br />
Sitting with your arms at your sides. The following are the positions of choice, however it is doubtful whether the
individual muscles can be separated when a vigorous effort is used. The brachialis particularly independent of the
position of the forearm
<ul>
<li>Biceps brachii: forearm supination</li>
<li>Brachial: forearm in pronation</li>
<li>Brachioradialis: forearm in the middle position between pronation and supination</li>
</ul>
<br />

<strong>Therapist position</strong>:<br />
Stand in front of the patient to the side to be tested. The hand that applies resistance is placed on the flexor
surface of the forearm proximal to the wrist. The other hand applies a counterforce by placing the palm over the
anterior and upper surfaces of the shoulder.<br />
No resistance is applied on a Grade 3 (Regular) test, however the elbow to be tested is held by the examiner's hand.
<br />

<strong>Test (for all positions of the forearm)</strong>:<br />
The patient flexes the elbow through the range of motion<br />

<strong>Instructions to the patient (all three tests)</strong>:<br />
Normal and good: "Bend your elbow, hold that position, do not let it push you down."<br />
Regular: "Bend your elbow."<br />
<br />

<div class="main-test">
<strong>For Precarious</strong>: Complete the partial range of motion (in each of the muscles tested)
</div>

<strong>Patient Position</strong>:<br />
All Flexors of the Elbow: Sitting with the arm abducted in 90° and supported by the examiner. The forearm is placed
supine (biceps), pronation (brachial), and in the middle (brachioradial) position.<br />

<strong>Alternative position</strong>:<br />
Supine. The elbow is flexed approximately 45° with the forearm in the position described for each of the muscles.<br />

<strong>Therapist position</strong>:<br />
All three flexors: standing and in front of the patient and supporting the abducted arm under the elbow and the wrist
if necessary. Palpate the biceps tendon in the antecubital space. At arm level, muscle fibers can be perceived on the
anterior surface of the middle two thirds with the short portion occupying a medial position in relation to the long
portion.<br />
Palpate the brachialis in the distal arm medial to the biceps tendon. Palpate the brachioradialis on the proximal
palmar surface of the arm, where it forms the lateral border of the ulnar force.<br />

<strong>Test</strong>:<br />
The patient tries to flex the elbow<br />

<strong>Instructions to the patient</strong>:<br />
"Try to bend your elbow."<br />
<br />

<div class="main-test">
<strong>For Trace</strong>: The examiner can palpate a contractile response on each of the muscles for which a stroke
degree is assigned<br />
<strong>Zero</strong>: No palpable contractile activity<br />
</div>

<strong>Patient Position</strong>:<br />
Dorsal decubitus for all three muscles. All other aspects are the same as the test grade 2 (Precarious)<br />

<strong>Therapist position</strong>:<br />
Standing on the side to be tested. All other aspects are the same as the test grade 2 (Precarious)<br />

<strong>Test</strong>:<br />
The patient tries to bend the elbow with the hand in supination, pronation and in the average position<br />
    """)

    TEXT_ELBOW_FLEXION_AFTER = _(u"""
<strong>USEFUL SUGGESTIONS</strong>
<ol>
<li>The patient's wrist flexor muscles should remain relaxed throughout the test because vigorous contraction of the
wrist flexors may assist in elbow flexion.</li>
<li>If the sitting position is contraindicated for any reason, all tests for these muscles may be performed in the
dorsal decubitus position, but in this case the manual resistance should be part of the Grade 3 (Regular) - gravity
compensation test.</li>
</ol>
    """)

    TEXT_ELBOW_EXTENSION = _(u"""
<div class="main-test">
<strong>To Normal</strong>: completes the available range and holds it firmly against a maximum resistance<br />
<strong>Good</strong>: completes the available amplitude against a significant resistance, but a "failure" of the
    resistance in the terminal amplitude is observed.<br />
<strong>Regular</strong>: Complete the available range without any manual resistance
</div>

<strong>Patient Position</strong>:<br />
Ventral rest on the table. The patient initiates the test with the arm at 90 ° of abduction and the forearm flexed
    and hung vertically over the side of the table.<br />

<strong>Therapist position</strong>:<br />
For the ventral decubitus patient the therapist provides support immediately above the elbow. The other hand is used
    to apply downward resistance on the dorsal surface of the wrist.<br />

<strong>Test</strong>:<br />
The patient extends the elbow to the end of the available range or until the forearm is horizontal in relation to the
    floor.<br />
<strong>Instructions to the patient</strong>:<br />
"Keep your elbow, hold that position, do not let me have it."<br />
<br />

<div class="main-test">
<strong>For precarious</strong>: Complete the available range in the absence of gravity<br />
<strong>Trace</strong>: The examiner may notice the tension in the triceps tendon immediately proximal to the olecranon
    or some contractile activity in the muscle fibers on the posterior surface of the arm.<br />
<strong>Zero</strong>: No evidence of any muscle activity
</div>

<strong>Patient Position</strong>:<br />
Seated. The arm is abducted by 90° with the shoulder in neutral rotation and the elbow flexed by approximately 45°.
        The member as a whole is horizontal in relation to the floor.<br />

<strong>Therapist position</strong>:<br />
Standing on the side of the patient being tested. For grade 2 test (precarious), support the limb at the level of the
        elbow. For test grade 1 (trace) or zero, support the limb under the forearm and palpate the triceps on the
        posterior surface of the arm immediately proximal to the olecranon.<br />

<strong>Test</strong>:<br />
The patient tries to extend the elbow.<br />

<strong>Instructions to the patient</strong>:<br />
"Try rectifying the elbow."<br />
    """)

    TEXT_ELBOW_EXTENSION_AFTER = _(u"""
<strong>REPLACEMENT BY BRAQUIAL BICEPS</strong>
<ol>
<li>Through external rotation. When the patient is seated with the abducted arm, the elbow extension can be performed
    with a triceps grade 0. This can occur when the patient rotates the shoulder externally, thereby allowing the arm
    to fall down below the forearm. As a result, the elbow falls literally.</li>
<li>Through horizontal adduction. This replacement can perform elbow extension and is purposely used by patients with
    a cervical cord injury and a grade 0 triceps. With the distal segment remaining (as occurs when the examiner
    stabilizes the hand or wrist), the patient performs adduction Horizontal of the arm, and this thrust places the
    elbow in extension. Therefore, the therapist should provide support at the level of the elbow rather than at the
    wrist level if the purpose is simply to test.</li>
</ol>
<br />

<strong>USEFUL SUGGESTIONS</strong>
<ol>
<li>The therapist must confirm that muscle activity is observed and perceived (that is, triceps activity actually
    exists), as patients often become addicted to substitution. In fact, substitutions are often taught and encouraged
    as a functional movement, but are not allowed for the purpose of performing the tests.</li>
<li>Apply resistance in grade 5 and 4 tests with the elbow flexed slightly to prevent the patient from "locking" the
    elbow joint through hyperextension.</li>
<li>Ideally, the elbow extension should not be tested in the position of the ventral decubitus, since when the shoulder
    is placed in horizontal abduction to perform the test, the biarticular muscle is less effective and the degree of
    the test may be lower than expected .</li>
<li>An alternative position for grades 5, 4, and 3 is with the patient just sitting. The examiner stands behind the
    patient, supporting the arm at 90 ° of abduction just above the flexed elbow. The patient grates the elbow against
    a resection applied at the wrist level.</li>
</ol>
    """)

    TEXT_FOREARM_SUPINATION = _(u"""
<div class="main-test">
<strong>To Normal</strong>: Completes the full range of motion available and maintains this position against maximum
    resistance.<br />
<strong>Good</strong>: Completes the full range of movement against a strong to moderate resistance.<br />
<strong>Regular</strong>: Complete the available range without any resistance.
</div>

<strong>Patient Position</strong>:<br />
Sitting, arm to the side and elbow flexed by 90 °; Forearm in the neutral or middle position. Alternatively, the
        patient may be seated at the table.<br />

<strong>Therapist position</strong>:<br />
Standing next to or in front of the patient. One hand holds the elbow. To apply resistance, hold the forearm by the
        palmar surface at the wrist level.<br />

<strong>Test</strong>:<br />
The patient begins in the neutral position of the wrist and performs supination of the forearm until the palm of the
        hand is directed towards the ceiling. The therapist resists movement in the direction of pronation. (No
        resistance is applied to Grade 3 - Regular).<br />

<strong>Alternative test</strong>:<br />
Hold the patient's hand as if shaking hands; Hold the elbow and resting through manual hold. This test is used when the
        patient has a grade 5 (Normal) or 4 (Good) wrist and hand strength. If wrist flexion is painful, apply wrist
        level restraint (a more difficult level).<br />

<strong>Instructions to the patient</strong>:<br />
"Turn your palm up, hold that position, do not let me turn it down, keep your wrists and fingers relaxed."<br />
For Grade 3 (Regular): "Turn your palm up."<br />
<br />

<div class="main-test">
<strong>For Precarious</strong>: Complete the partial range of motion
</div>

<strong>Patient Position</strong>:<br />
Sitting with the shoulder flexed between 45 ° and 90 ° and the elbow flexed by 90 °. Forearm in neutral position.<br />

<strong>Therapist position</strong>:<br />
Support the arm to be tested by opening the hand under the elbow.<br />

<strong>Test</strong>:<br />
The patient performs supination of the forearm through the partial range of motion.<br />

<strong>Instructions to the patient</strong>:<br />
"Turn your palm toward your face."<br />
<br />

<div class="main-test">
<strong>For Trace</strong>: Slight contractile activity, but no limb movement.<br />
<strong>Zero</strong>: No contractile activity<br />
</div>

<strong>Patient Position</strong>:<br />
Seated. Arm and elbow are flexed as is done for the Grade 3 (Regular) test.<br />

<strong>Therapist position</strong>:<br />
Support the forearm immediately below the elbow. Palpate the supinator distally to the radius head on the dorsal side
        of the forearm.<br />

<strong>Test</strong>:<br />
The patient tries to perform supination of the forearm.<br />

<strong>Instructions to the patient</strong>:<br />
"Try to turn the palm of your hand so that it faces the ceiling."
    """)

    TEXT_FOREARM_SUPINATION_AFTER = _(u"""
<strong>REPLACEMENT</strong>
<ol>
<li>The patient can rotate externally and perform the arm adduction through the body when supination of the forearm is
    attempted. When this occurs, the forearm enters supination without any activity of the supinator muscle.</li>
<li>The patient should be instructed to keep the wrist and fingers as relaxed as possible in order to avoid
    replacements, particularly by the wrist extensors.</li>
</ol>
    """)

    TEXT_FOREARM_PRONATION = _(u"""
<div class="main-test">
<strong>To Normal</strong>: Completes the available range of motion and holds against maximum resistance.<br />
<strong>Good</strong>: Completes all available range against strong to moderate resistivity.<br />
<strong>Regular</strong>: Complete the available range without any resistance.
</div>

<strong>Patient Position</strong>:<br />
Sitting at the table or in a chair with his arm resting on the table. Arm to side with elbow flexed 90 ° and forearm to
        neutral position.<br />

<strong>Therapist position</strong>:<br />
Standing next to or in front of the patient. Support the elbow. The hand used to apply resistance holds the forearm
        over the dorsal surface at the level of the wrist.<br />

<strong>Test</strong>:<br />
The patient begins with a neutral forearm position and performs pronation of the forearm until the palm of the hand is
        down. The therapist resists movement at the wrist level in the direction of supination for Grades 4 (Good) and
        5 (Normal).<br />
No restatement is applied for Grade 3 (regular).<br />
<strong>Alternative test</strong>:<br />
Hold the patient's hand as if to shake hands, keeping the elbow with the other hand and opposing pronation by
        hand-gripping. This alternative test can be used when the patient has a normal or good wrist and strength in
        the hand.<br />

<strong>Instructions to the patient</strong>:<br />
"Turn the palm of your hand down, hold that position. Do not let me radiate it up, keep your fist and your fingers
        relaxed."<br />
<br />

<div class="main-test">
<strong>For Preclear</strong>: Complete the partial range of motion
</div>

<strong>Patient Position</strong>:<br />
Sitting with the shoulder flexed between 45 ° and 90 ° and the elbow flexed by 90 °. The forearm is in the neutral
        position.<br />

<strong>Therapist position</strong>:<br />
Support the arm to be tested by placing the hand under the elbow.<br />
<strong>Test</strong>:<br />
The patient performs pronation of the forearm.<br />
<strong>Instructions to the patient</strong>:<br />
"Turn the palm of your hand by pointing it out in the opposite direction of your face."<br />

<div class="main-test">
<strong>For Trace</strong>: Contractile activity visible or palpable without any movement of the part.<br />
<strong>Zero</strong>: No contractile activity.
</div>

<strong>Patient Position</strong>:<br />
Seated. The arm is positioned as it is made for the Grade 3 (Regular) test.<br />
<strong>Therapist position</strong>:<br />
Support the forearm immediately below the elbow. The fingers of the other hand are used to palpate the pronator round
        about the upper third of the palmar surface of the forearm in a diagonal line from the medial condyle of the
        humerus to the lateral border of the radius.<br />
<strong>Test</strong>:<br />
The patient tries to perform the pronation of the forearm.<br />
<strong>Instructions to the patient</strong>:<br />
"Try to turn the palm of your hand down."<br />
    """)

    TEXT_FOREARM_PRONATION_AFTER = _(u"""
<strong>REPLACEMENT</strong><br />
The patient can rotate the shoulder internally or abduct it during pronation attempts. When this occurs, the forearm
        goes into pronation without the help of the activity performed by the pronator muscles.<br />
<br />

<strong>USEFUL SUGGESTIONS</strong><br />
The patient should be instructed to keep wrists and fingers relaxed in order to avoid replacement by the radial flexor
        of the carpus and flexors of the fingers.<br />
    """)

    TEXT_WRIST_FLEXION = _(u"""
<div class="main-test">
<strong>To Normal</strong>: Completes the available flexion span of the grip and holds that position against maximum
    resistance.<br />
<strong>Good</strong>: Complete the available range and maintain this position against a strong to moderate resistance.
</div>

<strong>Patient Position (All Tests)</strong>:<br />
Sitting, the forearm is supported on its dorsal surface on the table. To start, the forearm is supinated. The handle is
        in neutral or slightly extended position.<br />

<strong>Therapist position</strong>:<br />
One hand rests the patient's forearm under his wrist.<br />
<strong>To test both wrist flexors</strong>:<br />
The examiner holds the palm of the hand to be tested with the thumb circling the dorsal surface. The resitance is
        applied evenly through the hand in a straight downward direction toward the extension handle.<br />

<strong>To test the radial flexor of the carpus</strong>:<br />
The resistance is centered over the second metacarpal (radial side of the hand) in the direction of extension and ulnar
        deviation.<br />
<strong>To test the ulnar flexor of the carpus</strong>:<br />
The resistance is centered on the fifth metacarpal (ulnar side of the hand) in the direction of extension and radial
        deviation.<br />
<strong>Test</strong>:<br />
The patient flexes his fist, keeping his fingers and thumb relaxed.<br />
<strong>Patient Instructions (All tests)</strong>:<br />
"Do not let me push you down." Keep your fingers relaxed.<br />

<div class="main-test">
<strong>To Regular</strong>: Completes the available range without resting.
</div>

<strong>Patient Position (All Tests)</strong>:<br />
Initial position with supinated forearm and wrist in the neutral position as in the tests for Degrees 5 (Normal) and
        4 (Good). Sitting, the forearm is supported on its dorsal surface on the table. To start, the forearm is
        supinated. The handle is in neutral or slightly extended position.<br />

<strong>Therapist position</strong>:<br />
Support the patient's forearm under the wrist.<br />
<strong>Test</strong>:<br />
<div style="margin-right: 20px">
<strong>Both flexors of the wrist</strong>:<br />
The patient flexes the wrist directly upward without resting and without radial or ulnar deviation.<br />
<strong>For the radial flexor of the carpus</strong>:<br />
The patient flexes the wrist in radial deviation.<br />
<strong>For the ulnar flexor of the carpus</strong>:<br />
The patient flexed the wrist in ulnar deviation.<br />
</div>

<strong>Instructions to the patient</strong>:<br />
<div style="margin-right: 20px;">
<strong>Both flexors of the handle</strong>:<br />
"Bend your fist, keep it straight with your fingers relaxed."<br />
<strong>For the radial flexor of the carpus</strong>:<br />
"Bend your fist with your thumb facing sideways."<br />
<strong>For the ulnar flexor of the carpus</strong>:<br />
"Bend your fist toward the little finger."<br />
</div>

<div class="main-test">
<strong>For Precarious</strong>: Complete the available range of wrist flexion without assistance of gravity.
</div>

<strong>Patient Position</strong>:<br />
Sitting with his elbow resting on the table. Forearm in middle position with hand resting on ulnar side.<br />
<strong>Therapist position</strong>:<br />
Support the patient's forearm above the wrist.<br />
<strong>Test</strong>:<br />
The patient flexes the wrist with the ulnar surface by sliding through or without touching the table. To test the two
        wrist flexors separately, hold the forearm so that the wrist does not rest on the table and ask the patient to
        flex the wrist while the wrist is ulna and then radial.<br />

<strong>Instructions to the patient</strong>:<br />
"Bend your fist, keeping your fingers relaxed."<br />

<div class="main-test">
<strong>For Trace</strong>: One or both tendons may exhibit a visible or palpable contractile activity, but the part
    does not move.<br />
<strong>Zero</strong>: No contractile activity.
</div>

<strong>Patient Position</strong>:<br />
Supine forearm resting on the table.<br />
<strong>Therapist position</strong>:<br />
Support the wrist in flexion; The index finger of the other hand is used to palpate the appropriate tendons.<br />
Palpate the flexor tendons of the carpi radialis and ulnar flexor of the carpus in separate tests<br />
The radial flexor of the carpus is located on the lateral palmar aspect of the wrist laterally to the long palmar
        muscle if the patient possesses this muscle.<br />
The carpal ulnar flexor tendon is located on the palmar medial aspect of the wrist.<br />

<strong>Test</strong>:<br />
The patient tries to flex the wrist.<br />
<strong>Instructions to the patient</strong>:<br />
"Try to fold it in. Relax.<br />
The patient should be asked to repeat the test so that the examiner can perceive the tendons as much during relaxation
        s during contraction.<br />
    """)

    form = MRCForm
    fieldsets = (
        (_(u'Patient'), {
            'fields': ('patient', 'period'),
            'description': {
                'fieldset': '_patient',
            }
        }),
        (_('Shoulder abduction'), {
            'fields': (('shoulder_abduction_left', 'shoulder_abduction_right'), 'shoulder_abduction_obs'),
            'description': {
                'text': TEXT_SHOULDER_ABDUCTION,
                'text_after': TEXT_SHOULDER_ABDUCTION_AFTER,
                'fieldset': '_1col',
            }
        }),
        (_('Shoulder flexion'), {
            'fields': (('shoulder_flexion_left', 'shoulder_flexion_right'), 'shoulder_flexion_obs'),
            'description': {
                'text': TEXT_SHOULDER_FLEXION,
                'fieldset': '_1col',
            }
        }),
        (_('Shoulder lateral rotation'), {
            'fields': (('shoulder_lateral_rotation_left', 'shoulder_lateral_rotation_right'),
                       'shoulder_lateral_rotation_obs'),
            'description': {
                'text': TEXT_SHOULDER_LATERAL_ROTATION,
                'text_after': TEXT_SHOULDER_LATERAL_ROTATION_AFTER,
                'fieldset': '_1col',
            }
        }),
        (_('Elbow flexion'), {
            'fields': (('elbow_flexion_left', 'elbow_flexion_right'), 'elbow_flexion_obs'),
            'description': {
                'text': TEXT_ELBOW_FLEXION,
                'text_after': TEXT_ELBOW_FLEXION_AFTER,
                'fieldset': '_1col',
            }
        }),
        (_('Elbow extention'), {
            'fields': (('elbow_extension_left', 'elbow_extension_right'), 'elbow_extension_obs'),
            'description': {
                'text': TEXT_ELBOW_EXTENSION,
                'text_after': TEXT_ELBOW_EXTENSION_AFTER,
                'fieldset': '_1col',
            }
        }),
        (_('Forearm supination'), {
            'fields': (('forearm_supination_left', 'forearm_supination_right'), 'forearm_supination_obs'),
            'description': {
                'text': TEXT_FOREARM_SUPINATION,
                'text_after': TEXT_FOREARM_SUPINATION_AFTER,
                'fieldset': '_1col',
            }
        }),
        (_('Forearm pronation'), {
            'fields': (('forearm_pronation_left', 'forearm_pronation_right'), 'forearm_pronation_obs'),
            'description': {
                'text': TEXT_FOREARM_PRONATION,
                'text_after': TEXT_FOREARM_PRONATION_AFTER,
                'fieldset': '_1col',
            }
        }),
        (_('Wrist flexion'), {
            'fields': (('wrist_flexion_left', 'wrist_flexion_right'), 'wrist_flexion_obs'),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_('Wrist extension'), {
            'fields': (('wrist_extension_left', 'wrist_extension_right'), 'wrist_extension_obs'),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_('Fingers\' metacarpophalangeal flexion'), {
            'fields': (('fingers_mp_flexion_left', 'fingers_mp_flexion_right'), 'fingers_mp_flexion_obs'),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_('Fingers\' metacarpophalangeal extension'), {
            'fields': (('fingers_mp_extensor_left', 'fingers_mp_extensor_right'), 'fingers_mp_extensor_obs'),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_('Hip flexion'), {
            'fields': (('hip_flexion_left', 'hip_flexion_right'), 'hip_flexion_obs'),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_('Hip extension'), {
            'fields': (('hip_extension_left', 'hip_extension_right'), 'hip_extension_obs'),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_('Hip abduction'), {
            'fields': (('hip_abduction_left', 'hip_abduction_right'), 'hip_abduction_obs'),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_('Hip medial rotation'), {
            'fields': (('hip_medial_rotation_left', 'hip_medial_rotation_right'), 'hip_medial_rotation_obs'),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_('Hip lateral rotation'), {
            'fields': (('hip_lateral_rotation_left', 'hip_lateral_rotation_right'), 'hip_lateral_rotation_obs'),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_('Knee extension'), {
            'fields': (('knee_extension_left', 'knee_extension_right'), 'knee_extension_obs'),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_('Knee flexion'), {
            'fields': (('knee_flexion_biceps_left', 'knee_flexion_biceps_right'), 'knee_flexion_biceps_obs',
                       ('knee_flexion_semitendinosus_g5_left', 'knee_flexion_semitendinosus_g5_right'),
                       'knee_flexion_semitendinosus_g5_obs',
                       ('knee_flexion_semitendinosus_g2_left', 'knee_flexion_semitendinosus_g2_right'),
                       'knee_flexion_semitendinosus_g2_obs',
                       ),
            'description': {
                'fieldset': '_1col_divide',
            }
        }),
        (_('Ankle plantar flexion'), {
            'fields': (('ankle_plantar_flexion_gastrocnemius_g5_left', 'ankle_plantar_flexion_gastrocnemius_g5_right'),
                       'ankle_plantar_flexion_gastrocnemius_g5_obs',
                       ('ankle_plantar_flexion_sole_g5_left', 'ankle_plantar_flexion_sole_g5_right'),
                       'ankle_plantar_flexion_sole_g5_obs',
                       ('ankle_plantar_flexion_sole_g2_left', 'ankle_plantar_flexion_sole_g2_right'),
                       'ankle_plantar_flexion_sole_g2_obs',
                       ),
            'description': {
                'fieldset': '_1col_divide',
            }
        }),
        (_('Ankle dorsiflexion and subtalar inversion'), {
            'fields': (('ankle_dorsiflexion_left', 'ankle_dorsiflexion_right'),
                       ('ankle_subtalar_inversion_left', 'ankle_subtalar_inversion_right'),
                       'ankle_dorsiflexion_subtalar_inversion_obs'),
            'description': {
                'fieldset': '_1col_divide',
            }
        }),
        (_('Subtalar inversion'), {
            'fields': (('subtalar_inversion_left', 'subtalar_inversion_right'), 'subtalar_inversion_obs'),
            'description': {
                'fieldset': '_1col',
            }
        }),
        (_('Subtalar eversion'), {
            'fields': (('subtalar_eversion_left', 'subtalar_eversion_right'), 'subtalar_eversion_obs'),
            'description': {
                'fieldset': '_1col',
            }
        }),
    )

    list_display = ('patient', 'period', 'last_update')
    ordering = ('patient', 'period', 'last_update')

admin.site.register(MRC, MRCAdmin)

x = _(u"""
<div class="main-test">
<strong>Para Normal</strong>: Completa a amplitude disponível de flexão do punho e mantém essa posição contra uma
    resistência máxima.<br />
<strong>Bom</strong>: completa a amplitude disponível e mantém essa posição contra uma ressitência de forte a moderada.
    <br />
</div>

<strong>Posição do paciente (Todos os testes)</strong>:<br />
Sentado, o antebraço é apoiado em sua superfície dorsal sobre a mesa. Para iniciar, o antebraço é supinado. O punho
        fica na posição neutra ou ligeiramente estendido.<br />

<strong>Posição do terapeuta</strong>:<br />
Uma das mãos apoia o antebraço do paciente debaixo do punho.<br />
<strong>Para testar ambos os flexores do punho</strong>:<br />
O examinador segura a palma da mão a ser testada com o polegar circundando a superfície dorsal. A ressitência é
    aplicada uniformemente através da mão numa direção diretamente para baixo no sentido do punho em extensão.<br />

<strong>Para testar o flexor radial do carpo</strong>:<br />
A resistência é centralizada sobre o segundo metacarpo (lado radial da mão) na direção da extensão e do desvio ulnar.
<br />
<strong>Para testar o flexor ulnar do carpo</strong>:<br />
A resistência é centralizada sobre o quinto metacarpo (lado ulnar da mão) na direção da extensão e do desvio radial.
<br />
<strong>Teste</strong>:<br />
O paciente flexiona o punho, mantendo os dedos e polegar relaxados.<br />
<strong>Instruções ao paciente (Todos os testes)</strong>:<br />
"Dobre o punho. Mantenha essa posição. Não me permita empurrá-lo para baixo. Mantenha seus dedos relaxados."<br />

<div class="main-test">
<strong>Para Regular</strong>: Completa a amplitude disponível sem resistência.
</div>

<strong>Posição do paciente (Todos os testes)</strong>:<br />
Posição inicial com o antebraço supinado e punho na posição neutra como nos testes para os Graus 5 (Normal) e 4 (Bom).
        Sentado, o antebraço é apoiado em sua superfície dorsal sobre a mesa. Para iniciar, o antebraço é supinado.
        O punho fica na posição neutra ou ligeiramente estendido.<br />

<strong>Posição do terapeuta</strong>:<br />
Apoia o antebraço do paciente debaixo do punho.<br />
<strong>Teste</strong>:<br />
<div style="margin-right: 20px">
<strong>ambos os flexores do punho</strong>:<br />
O paciente flexiona o punho diretamente para cima sem resistência e sem desvio radial ou ulnar.<br />
<strong>Para o flexor radial do carpo</strong>:<br />
O paciente flexiona o punho em desvio radial.<br />
<strong>Para o flexor ulnar do carpo</strong>:<br />
O paciente flexionada o punho em desvio ulnar.<br />
</div>
<strong>Instruções ao paciente</strong>:<br />
<div style="margin-right: 20px">
<strong>ambos os flexores do punho</strong>:<br />
"Dobre o punho, mantenha-o retificado com os dedos relaxados."<br />
<strong>Para o flexor radial do carpo</strong>:<br />
"Dobre o punho com o polegar orientado para o lado."<br />
<strong>Para o flexor ulnar do carpo</strong>:<br />
"Dobre o punho na direção do dedo mínimo."<br />
</div>
<br />
<div class="main-test">
<strong>Para Precário</strong>: Completa a amplitude disponível de flexão do punho sem assistência da gravidade.
</div>

<strong>Posição do paciente</strong>:<br />
Sentado com o cotovelo apoiado sobre a mesa. Antebraço na posição média com a mão apoiada sobre o lado ulnar.<br />
<strong>Posição do terapeuta</strong>:<br />
Apoia o antebraço do paciente acima do punho.<br />
<strong>Teste</strong>:<br />
O paciente flexiona o punho com a superfície ulnar deslizando através da ou sem tocar na mesa. Para testar
        separadamente os dois flexores do punho, segurar o antebraço de forma que o punho não fique sobre a mesa e
        pedir ao paciente que realize o movimento de flexão enquanto o punho está em desvio ulna e, a seguir, radial.
<br />

<strong>Instruções ao paciente</strong>:<br />
"Dobre o punho, mantendo seus dedos relaxados."<br />
<br />

<div class="main-test">
<strong>Para Traço</strong>:  Um ou ambos os tendões podem exibir uma atividade contrátil visível ou palpável, porém a
    parte não se movimenta.<br />
<strong>Zero</strong>: Nenhuma atividade contrátil.
</div>

<strong>Posição do paciente</strong>:<br />
Antebraço supinado apoiado sobre a mesa.<br />
<strong>Posição do terapeuta</strong>:<br />
Apoiar o punho em flexão; o dedo indicador da outra mão é usado para palpar os tendões apropriados.<br />
Palpar os tendões do flexor radial do carpo e do flexor ulnar do carpo em testes separados.<br />
O flexor radial do carpo está localizado na face palmar lateral do punho lateralmente ao musculo palmar longo, se o
        paciente possuir este músculo.<br />
O tendão do flexor ulnar do carpo está localizado na face palmar medial do punho.<br />

<strong>Teste</strong>:<br />
O paciente tenta flexionar o punho.<br />
<strong>Instruções ao paciente</strong>:<br />
"Tente dobrar o punho. Relaxar. Dobrá-lo novamente."<br />
Deve-se pedir ao paciente que repita o teste, para que o examinador possa perceber os tendões tanta durante o
        relaxamento quanto durante a contração.<br />
""")